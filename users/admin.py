from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'teacher_id', 'nid', 'class_name', 'class_roll', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

    def get_queryset(self, request):
        return super().get_queryset(request)

    def teacher_id(self, obj):
        # Display teacher_id only if role is teacher
        if obj.role == 'teacher':
            return obj.teacher_id if obj.teacher_id else 'N/A'
        return 'N/A'

    def nid(self, obj):
        # Display nid only if role is teacher
        if obj.role == 'teacher':
            return obj.nid if obj.nid else 'N/A'
        return 'N/A'

    def class_name(self, obj):
        # Display class_name only if role is student
        if obj.role == 'student':
            return obj.class_name if obj.class_name else 'N/A'
        return 'N/A'

    def class_roll(self, obj):
        # Display class_roll only if role is student
        if obj.role == 'student':
            return obj.class_roll if obj.class_roll else 'N/A'
        return 'N/A'

# Register the User model with the custom admin
admin.site.register(User, UserAdmin)
