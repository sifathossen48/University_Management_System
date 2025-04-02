from django.urls import path
from .views import (
    AdminRegisterView,
    LoginView,
    LogoutView,
    StudentRegisterView,
    TeacherRegisterView,
    LibrarianRegisterView
)

urlpatterns = [
    path('register/admin/', AdminRegisterView.as_view(), name='register-admin'),
    path('register/student/', StudentRegisterView.as_view(), name='register-student'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='register-teacher'),
    path('register/librarian/', LibrarianRegisterView.as_view(), name='register-librarian'),
    path("login/", LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]