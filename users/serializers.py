from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
class BaseUserSerializer(serializers.ModelSerializer):
    """Base serializer for all user types"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AdminRegisterSerializer(BaseUserSerializer):
    """Serializer for Admin registration"""
    def create(self, validated_data):
        validated_data['role'] = 'admin'
        return super().create(validated_data)

class StudentRegisterSerializer(BaseUserSerializer):
    """Serializer for Student registration"""
    class_name = serializers.CharField(required=True)
    class_roll = serializers.IntegerField(required=True)

    class Meta:
        model = get_user_model() 
        fields =  ['username', 'email', 'password', 'role', 'class_name', 'class_roll']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        validated_data['role'] = 'student'
        
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'student')  
        )
        
        user.class_name = validated_data['class_name']
        user.class_roll = validated_data['class_roll']
        
        user.save() 
        
        return user

class TeacherRegisterSerializer(serializers.ModelSerializer):
    """Serializer for Teacher registration"""
    teacher_id = serializers.CharField(required=True)
    nid = serializers.CharField(required=True)

    class Meta:
        model = get_user_model()  # Use the custom User model
        fields = ['username', 'email', 'password', 'role', 'teacher_id', 'nid']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Add the teacher-specific fields and set the role to 'teacher'
        validated_data['role'] = 'teacher'
        
        # Create the User instance first
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'teacher')  # Default to 'teacher'
        )

        # Now set the teacher-specific fields (teacher_id, nid) manually
        user.teacher_id = validated_data['teacher_id']
        user.nid = validated_data['nid']
        
        user.save()  # Save the user instance with updated teacher-specific fields
        
        return user

class LibrarianRegisterSerializer(BaseUserSerializer):
    """Serializer for Librarian registration"""
    def create(self, validated_data):
        validated_data['role'] = 'librarian'
        return super().create(validated_data)
