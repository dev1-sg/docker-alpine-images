import locale
from datetime import datetime
from jinja2 import Template
from pathlib import Path

DOCKER_IMAGE_GROUP = input("Enter DOCKER_IMAGE_GROUP: ").strip()
DOCKER_IMAGE = input("Enter DOCKER_IMAGE: ").strip()

now = datetime.now().astimezone()
updated_time = now.strftime("%c"), now.tzname()
template_vars = {
    "updated_at": updated_time,
    "DOCKER_IMAGE_GROUP": DOCKER_IMAGE_GROUP,
    "DOCKER_IMAGE": DOCKER_IMAGE,
}

TEMPLATES_DIR = Path("templates")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_template(filename: str) -> Template:
    path = TEMPLATES_DIR / filename
    with open(path) as f:
        return Template(f.read(), trim_blocks=True, lstrip_blocks=True)

def render_to_file(template: Template, output_path: Path, context: dict):
    rendered = template.render(context)
    with open(output_path, "w") as f:
        f.write(rendered)
    print(f"Generated {output_path}")

def generate_docs():
    template = load_template("docs_template.j2")
    output_path = OUTPUT_DIR / f"query-{DOCKER_IMAGE}-image.py"
    render_to_file(template, output_path, template_vars)

def generate_gh_action_pr():
    template = load_template("gh_action_pr_template.j2")
    output_path = OUTPUT_DIR / f"pr-dependabot-{DOCKER_IMAGE}.yml"
    render_to_file(template, output_path, template_vars)

def generate_gh_action_push():
    template = load_template("gh_action_push_template.j2")
    output_path = OUTPUT_DIR / f"push-{DOCKER_IMAGE}.yml"
    render_to_file(template, output_path, template_vars)

def generate_testcontainer():
    template = load_template("testcontainer_template.j2")
    output_path = OUTPUT_DIR / f"test_{DOCKER_IMAGE}.go"
    render_to_file(template, output_path, template_vars)

def main():
    print("Generating scaffold files...\n")
    generate_docs()
    generate_gh_action_pr()
    generate_gh_action_push()
    generate_testcontainer()
    print("\nAll files generated in:", OUTPUT_DIR.resolve())

if __name__ == "__main__":
    main()
