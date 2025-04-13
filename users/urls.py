from django.urls import path
from .views import (
    AdminDashboardView,
    AdminRegisterView,
    AnonymousDashboardView,
    LibrarianDashboardView,
    LoginView,
    LogoutView,
    StudentDashboardView,
    StudentRegisterView,
    TeacherDashboardView,
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
    path("dashboard/admin/", AdminDashboardView.as_view(), name="admin-dashboard"),
    path("dashboard/teacher/", TeacherDashboardView.as_view(), name="teacher-dashboard"),
    path("dashboard/student/", StudentDashboardView.as_view(), name="student-dashboard"),
    path("dashboard/librarian/", LibrarianDashboardView.as_view(), name="librarian-dashboard"),
    path("dashboard/public/", AnonymousDashboardView.as_view(), name="anonymous-dashboard"),
    
]