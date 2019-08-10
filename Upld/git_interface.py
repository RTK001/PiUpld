import git
import os

def validate_git_url(url):
    '''
    Runs ls-remote on url.
    If ls-remote returns a GitCommandError, the url is invalid.
    Otherwise, the url is valid.
    '''
    g = git.cmd.Git()
    try:
        heads = g.ls_remote(url)
        return True
    except git.exc.GitCommandError:
        return False


def clone_repo(url, path):
    '''
    Currently creates a clone from the URL with no processing, etc.
    '''
    clone = git.Repo.clone_from(url, path)
    return clone
