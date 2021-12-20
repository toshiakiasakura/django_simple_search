from celery import shared_task
import git

@shared_task
def renew_words():
    repo = git.Repo("../medical_words")
    repo.remotes.origin.pull()