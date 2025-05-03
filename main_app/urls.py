from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("contact/", views.contact),
    path("get_all_persons/", views.get_all_persons)
]