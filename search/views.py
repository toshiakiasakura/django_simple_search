from typing import Union, Optional, List, Dict, Tuple, Any
import os 

import logging
from django.shortcuts import render
from django.views import generic, View

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class AllWordView(generic.TemplateView):
    template_name = "all_word.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        with open("../medical_words/medical_words.txt") as f:
            data = f.read()
        kwargs["words"] = data.replace("\n", "<br>").replace(" ", "&nbsp;")
        return super().get_context_data(**kwargs)
