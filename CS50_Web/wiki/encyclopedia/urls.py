from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.new, name="new"),
    path("search/", views.search, name="search"),
    path("search/new", views.new, name="new"),
    path("new", views.new, name="new"),
    path("wiki/<str:page>", views.greet, name="greet"),
    path("edit/<str:page>", views.edit, name="edit"),
    path("saving", views.savig, name="saving"),
    path("random", views.random_page, name="random"),
    path("<str:page>", views.error, name="error"),
]
 