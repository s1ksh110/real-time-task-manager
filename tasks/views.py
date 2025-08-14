from django.shortcuts import render

# Create your views here.
# tasks/views.py
# Views handle HTTP requests and return responses.

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in output.

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# ... (keep existing imports and RegisterView)

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True  # Anyone can read.
        return obj.assigned_to == request.user  # Only owner can edit/delete.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]  # Require login, owner check.

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)  # Auto-assign to current user.

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)  # Only show user's tasks.