from github import Github
import typer

from racoon.template_generation import Context
from racoon.template_generation import generate_template

app = typer.Typer()


@app.command()
def generate(
    github_access_token: str = typer.Option(..., envvar="GITHUB_ACCESS_TOKEN"),
    project_name: str = typer.Option(...),
    src_dir: str = typer.Option("src"),
    template_url: str = typer.Option("https://github.com/nymann/python-template.git"),
) -> None:
    github = Github(login_or_token=github_access_token)
    config = Context(github=github, repo_name=project_name, src_dir=src_dir)
    generate_template(template_url=template_url, context=config)


if __name__ == "__main__":
    app()
