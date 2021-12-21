from celery import shared_task
import git

import os
from . import views

@shared_task
def renew_words():
    # TO DO: view.WORD_DIR is not found via celery. Problems are not solved yet.
    repo = git.Repo(views.WORD_DIR)
    res = repo.remotes.origin.pull()
    return True