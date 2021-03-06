from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
  path("", views.IndexView.as_view(), name="index" ),
  path("all_word", views.AllWordView.as_view(), name="all_word"),
  path("search", views.search_word, name="search_word"),
  path("update_file", views.update_file, name="update_file"),
]