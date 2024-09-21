from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path("category/<str:category>", views.category, name="category"),
    path("service/<int:service_id>", views.service, name="service"),
    path("upgrade", views.upgrade, name="upgrade"),
    path("professional/<str:professional_username>", views.professional, name="professional"),
    path("add_service", views.add_service, name="add_service"),
    path("service/<int:service_id>/book_slot/", views.book_slot, name="book_slot"),
    path("appointment/<int:service_id>", views.appointments, name="appointments"),
    path("booked", views.booked, name="booked"),
]