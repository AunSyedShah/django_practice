from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact),
    path("get_all_persons/", views.get_all_persons),
    path("delete_person/<str:id>", views.delete_person),
    path("update_person/<str:id>", views.update_person),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up")
]