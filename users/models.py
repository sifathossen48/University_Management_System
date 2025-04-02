from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('librarian', 'Librarian'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    teacher_id = models.CharField(max_length=100, blank=True, null=True)
    nid = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    class_roll = models.CharField(max_length=100, blank=True, null=True)
    
    def clean(self):
        """Ensure necessary fields are provided based on the user's role."""
        if self.role == 'teacher':
            if not self.teacher_id or not self.nid:
                raise ValidationError("Teacher must provide both teacher_id and nid.")
        
        if self.role == 'student':
            if not self.class_name or not self.class_roll:
                raise ValidationError("Student must provide both class_name and class_roll.")

    def __str__(self):
        return self.username