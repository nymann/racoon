import string

from cookiecutter.main import cookiecutter
from github import Github


class Context:
    def __init__(self, github: Github, repo_name: str, src_dir: str) -> None:
        self._github = github
        user = self._github.get_user()
        self.git_registry = "https://github.com/"
        repo_name = repo_name.lower()
        for ch in repo_name:
            if ch not in string.ascii_lowercase:
                repo_name = repo_name.replace(ch, "-")

        self.repo_name = repo_name
        self.project_slug = repo_name.replace("-", "_")
        self.project_name = " ".join(word.capitalize() for word in repo_name.split("-"))
        self.author_email = user.email
        self.author_name = user.name
        self.git_registry_account = user.login
        self.src_dir = src_dir

    def dict(self) -> dict[str, str]:
        return {
            "repo_name": self.repo_name,
            "project_name": self.project_name,
            "project_slug": self.project_slug,
            "author_name": self.author_name,
            "author_email": self.author_email,
            "git_registry": self.git_registry,
            "git_registry_account": self.git_registry_account,
            "src_dir": self.src_dir,
        }


def generate_template(template_url: str, context: Context):
    cookiecutter(
        template=template_url,
        extra_context=context.dict(),
        no_input=True,
    )
