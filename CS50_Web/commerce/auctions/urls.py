from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("auction/<int:auction_id>", views.auction_detail, name="auction_detail"),
    path("categories/auction/<int:auction_id>", views.auction_detail, name="auction_detail"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:auction_category>", views.kategorie, name="kategorie")
]
