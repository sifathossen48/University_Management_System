from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .decorators import role_required
from .serializers import (
    AdminRegisterSerializer,
    StudentRegisterSerializer,
    TeacherRegisterSerializer,
    LibrarianRegisterSerializer
)

class AdminRegisterView(generics.CreateAPIView):
    """Register an Admin"""
    queryset = User.objects.all()
    serializer_class = AdminRegisterSerializer
    permission_classes = [AllowAny]

class StudentRegisterView(generics.CreateAPIView):
    """Register a Student"""
    queryset = User.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = [AllowAny]

class TeacherRegisterView(generics.CreateAPIView):
    """Register a Teacher"""
    queryset = User.objects.all()
    serializer_class = TeacherRegisterSerializer
    permission_classes = [AllowAny]

class LibrarianRegisterView(generics.CreateAPIView):
    """Register a Librarian"""
    queryset = User.objects.all()
    serializer_class = LibrarianRegisterSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Check if username and password are provided
        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "role": user.role  # Return user role (this assumes 'role' is a field in your User model)
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Blacklist the refresh token
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()  
            return Response({"message": "Successfully logged out!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        

class AdminDashboardView(APIView):
    """Dashboard for Admin"""
    @role_required("admin")
    def get(self, request):
        return Response({"message": "Welcome to the Admin Dashboard!", "role": request.user.role})

class TeacherDashboardView(APIView):
    """Dashboard for Teachers"""
    @role_required("teacher")
    def get(self, request):
        return Response({"message": "Welcome to the Teacher Dashboard!", "role": request.user.role})

class StudentDashboardView(APIView):
    """Dashboard for Students"""
    @role_required("student")
    def get(self, request):
        return Response({"message": "Welcome to the Student Dashboard!", "role": request.user.role})

class LibrarianDashboardView(APIView):
    """Dashboard for Librarians"""
    @role_required("librarian")
    def get(self, request):
        return Response({"message": "Welcome to the Librarian Dashboard!", "role": request.user.role})

class AnonymousDashboardView(APIView):
    """Dashboard for Anonymous Users"""
    permission_classes = [AllowAny]
    def get(self, request):
        if request.user.is_authenticated:
            # User is authenticated, show a message for logged-in users
            return Response({
                "message": "You are already logged in. You cannot access the public dashboard."
            })
        else:
            # User is not authenticated, show a message for unauthenticated users
            return Response({
                "message": "Welcome to the public dashboard! Please log in to access more features."
            })