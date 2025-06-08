REGISTRY_FULL_URI = "public.ecr.aws/dev1-sg/base/alpine:latest"
OUTPUT_DIR = Path("../src/alpine")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

import docker
from pathlib import Path

client = docker.from_env()
image_name = REGISTRY_FULL_URI

print(f"Pulling image: {image_name}")
image = client.images.pull(image_name)

image_details = client.images.get(image.id)
arch = image_details.attrs.get("Architecture", "unknown")

print(f"Detected architecture: {arch}")

def arch_file(filename_base):
    return OUTPUT_DIR / f"{filename_base}_{arch}.txt"

# 1. Get /etc/os-release
print("Collecting /etc/os-release...")
os_release_output = client.containers.run(
    image=image_name,
    command="cat /etc/os-release",
    remove=True,
    platform=f"linux/{arch}"
)
with open(arch_file("os_release"), "wb") as f:
    f.write(os_release_output)
print(f"/etc/os-release saved to {arch_file('os_release')}")

# 2. Get environment variables
print("Collecting environment variables...")
env_output = client.containers.run(
    image=image_name,
    command="env",
    remove=True,
    platform=f"linux/{arch}"
)
with open(arch_file("env"), "wb") as f:
    f.write(env_output)
print(f"Environment variables saved to {arch_file('env')}")

# 3. Get installed packages
print("Collecting installed packages...")
pkg_output = client.containers.run(
    image=image_name,
    command="apk info -v",
    remove=True,
    platform=f"linux/{arch}"
)
with open(arch_file("package"), "wb") as f:
    f.write(pkg_output)
print(f"Installed packages saved to {arch_file('package')}")
