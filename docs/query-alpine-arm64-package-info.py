DOCS_OUTPUT = "../src/alpine/package_arm64.txt"
REGISTRY_ARCH = "linux/arm64"
REGISTRY_FULL_URI = "public.ecr.aws/dev1-sg/base/alpine:latest"

import docker

client = docker.from_env()

image_name = REGISTRY_FULL_URI
platform = REGISTRY_ARCH

print(f"Pulling image: {image_name} for platform {platform}")
client.images.pull(image_name, platform=platform)

output = client.containers.run(
    image=image_name,
    command="apk info -v",
    remove=True,
    platform=platform
)

output_file = DOCS_OUTPUT

with open(output_file, "wb") as f:
    f.write(output)

print(f"Output saved to {output_file}")
