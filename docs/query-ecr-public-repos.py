import os
import boto3
from botocore.config import Config
from jinja2 import Template

REGISTRY_ALIAS = "dev1-sg"
REGISTRY_URI = f"public.ecr.aws/{REGISTRY_ALIAS}"

def load_template(file_path):
    with open(file_path, "r") as f:
        return f.read()

def get_public_ecr_client():
    session = boto3.Session()
    client = session.client(
        "ecr-public",
        region_name="us-east-1",
        endpoint_url="https://ecr-public.us-east-1.amazonaws.com",
        config=Config(signature_version='v4')
    )
    return client

def get_repositories(client):
    repos = []
    paginator = client.get_paginator("describe_repositories")
    for page in paginator.paginate():
        repos.extend(page.get("repositories", []))
    return repos

def get_latest_tags(client, repo_name):
    try:
        resp = client.describe_images(repositoryName=repo_name)
        tags = []
        for img in resp.get("imageDetails", []):
            for tag in img.get("imageTags", []):
                if tag == "latest" or any(c in tag for c in ["1.", "2.", "3.", "bookworm"]):
                    tags.append(tag)
        return sorted(set(tags))
    except Exception as e:
        print(f"[Warning] Failed to fetch tags for {repo_name}: {e}")
        return ["N/A"]

def main():
    template_str = load_template("template.j2")
    client = get_public_ecr_client()
    repos = get_repositories(client)
    repos.sort(key=lambda r: r["repositoryName"])
    data = []
    for idx, repo in enumerate(repos, start=1):
        name = repo["repositoryName"]
        group = name.split("/")[0] if "/" in name else "-"
        uri = f"{REGISTRY_URI}/{name}"
        tags = get_latest_tags(client, name)
        data.append({
            "number": idx,
            "name": name,
            "group": group,
            "uri": uri,
            "tags": tags,
        })
    template = Template(template_str.strip())
    output = template.render(items=data)
    print(output)
    with open("ecr_public_repos.md", "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()
