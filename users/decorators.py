from functools import wraps
from rest_framework.response import Response
from rest_framework import status


def role_required(role):
    """Decorator to check if the user has the required role."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, request, *args, **kwargs):
            if request.user.role != role:
                return Response({"error": f"Only {role}s can perform this action."}, status=status.HTTP_403_FORBIDDEN)
            return view_func(self, request, *args, **kwargs)
        return wrapped_view
    return decorator

