
from django.urls import path

from . import views

urlpatterns = [
    path('data-url/', views.json_view, name="data-url"),
    path('data-url/<int:post_id>/', views.post_detail_view, name="post_detail"),
    path("show_like/", views.show_like, name="show_like"),
    path("show_like/<int:post_id>", views.like_detail, name="like_detail"),
    path("save_like/", views.save_like, name="save_like"),
    path("save-data/", views.save_data, name="save_data"),
    path("create_like/", views.create_like, name="create_like"),
    path("change_like/", views.change_like, name="change_like"),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("<str:user_username>/", views.about, name="about"),
    path("following", views.following, name="following"),
]
