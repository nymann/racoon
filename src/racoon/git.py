import os
import subprocess

from github.Repository import Repository


def init_template(repository: Repository) -> None:
    os.chdir(repository.name)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", ":tada: Initialize template nymann/python-template"])
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "origin",
            repository.ssh_url,
        ]
    )
    subprocess.run(["git", "push", "-u", "origin", "master"])
