"""
import os
import subprocess

from typing import Union

def git_init(repo_path:str):
    subprocess.run(["git", "init"], cwd=repo_path)

def git_add_remote(username:str, token:str, git_repo:str, local_repo_path:str):
    repo_url = 'https://{}:{}@github.com/{}'.format(username, token, git_repo)
    subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=local_repo_path)

def git_pull(repo_path:str):
    subprocess.run(["git", "pull"], cwd=repo_path)

def git_add(repo_path:str, files_to_add:Union[str, list[str]]):
    subprocess.run(["git", "add", "files_to_add"], cwd=repo_path)

def git_commit(repo_path:str, commit_message:str):
    subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path)

def git_push(repo_path:str, branch:str):
    subprocess.run(["git", "push", "--set-upstream", "origin", branch], cwd=repo_path)
"""