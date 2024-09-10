from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.student_register, name="student_register"),
    path("activate/<str:uid64>/<str:token>/", views.activate, name="activate"),
    path("logout/", views.user_logout, name="student_logout"),
    path("login/", views.user_login, name="student_login"),
]
