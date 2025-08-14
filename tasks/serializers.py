# tasks/serializers.py
# Serializers handle data validation and conversion between Python objects and JSON.

from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Only expose safe fields.

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)  # Nested serializer for user details.

    class Meta:
        model = Task
        fields = '__all__'  # Include all model fields in API.
        read_only_fields = ['created_at', 'updated_at']  # Auto fields can't be set manually.