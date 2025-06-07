import docker

client = docker.from_env()

image_name = "public.ecr.aws/dev1-sg/base/alpine:latest"
platform = "linux/amd64"

print(f"Pulling image: {image_name} for platform {platform}")
client.images.pull(image_name, platform=platform)

output = client.containers.run(
    image=image_name,
    command="apk info -v",
    remove=True,
    platform=platform
)

output_file = "../src/alpine/amd64_apk_info.md"

with open(output_file, "wb") as f:
    for pkg in output.split(b" "):
        f.write(pkg + b"\n")

print(f"Output saved to {output_file}")
