from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("check-room", views.check_room, name='check-room'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("apartment", views.apartment, name = 'apartment'),
    path("contact", views.contact, name = 'contact'),
    # comment 
]
