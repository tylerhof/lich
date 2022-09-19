import git
from git import Repo
import crypto_hofmetyl as crypto
import logging

def clone(git_url, repo_dir, password):
    Repo.clone_from(git_url, repo_dir)
    crypto.decrypt(repo_dir, password)

def push(repo_dir, commit_message, password):
    repo = git.Repo(repo_dir)
    crypto.encrypt(repo_dir, password)
    try:
        add_and_commit(repo, commit_message)
        origin = repo.remote(name='origin')
        origin.push().raise_if_error()
    except:
        logging.exception("message")
    crypto.decrypt(repo_dir, password)

def add_and_commit(repo, commit_message):
    repo.git.add(u=True)
    repo.index.commit(commit_message)

def pull(repo_dir, password):
    repo = git.Repo(repo_dir)
    repo.git.reset('--hard')
    origin = repo.remote(name='origin')
    origin.fetch()
    origin.pull("--rebase")
    crypto.decrypt(repo_dir, password)

#clone("https://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@github.com/tylerhof/evenMoreKewlRepository.git", "/home/tyler/PycharmProjects/utils/test6", "purpleMonkeyDishwasher1990Why")
#clone("https://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@github.com/tylerhof/evenMoreKewlRepository.git", "/home/tyler/PycharmProjects/utils/test7", "purpleMonkeyDishwasher1990Why")
#push("/home/tyler/PycharmProjects/utils/test6", "add additional line", "purpleMonkeyDishwasher1990Why")
pull("/home/tyler/PycharmProjects/utils/test7", "purpleMonkeyDishwasher1990Why")
https://github.com/tylerhof/crypto.git
https://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@github.com/tylerhof/crypto.git