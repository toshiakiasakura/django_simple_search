from typing import Union, Optional, List, Dict, Tuple, Any
import os 
import subprocess

import logging
from django.shortcuts import render
from django.views import generic, View

logger = logging.getLogger(__name__)
WORD_DIR = "../medical_words/"
WORD_FILE = WORD_DIR + "medical_words.txt"
WORD_TMP_FILE = WORD_DIR + "tmp.txt"

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class AllWordView(generic.TemplateView):
    template_name = "all_word.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        with open( WORD_FILE) as f:
            data = f.read()
        kwargs["words"] = modify_file2html(data)
        return super().get_context_data(**kwargs)

def search_word(request):
    data = "No search"
    word = "Missing"
    if request.method == "POST":
        word = request.POST["search_word"]
        try:
            data = subprocess.check_output(["grep", word, WORD_FILE,"-C10"]).decode()
            data = modify_file2html(data)
        except:
            data = "No result"
    return render(request, "search.html", {"words":data, "search_word": word})

def modify_file2html(s:str):
    return s.replace("\n", "<br>").replace(" ", "&nbsp;")

