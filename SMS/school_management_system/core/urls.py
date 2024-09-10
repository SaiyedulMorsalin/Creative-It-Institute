from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_profile, name="student_profile"),
    path("home/", views.home_page, name="home_page"),
]
