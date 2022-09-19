from .api import clone, push, pull

class Lich(object):

    def __init__(self, repo_dir, password):
        self.repo_dir = repo_dir
        self.password = password

    def clone(self, git_url):
        clone(git_url, self.repo_dir, self.password)

    def push(self, commit_message):
        push(self.repo_dir, commit_message, self.password)

    def pull(self):
        pull(self.repo_dir, self.password)