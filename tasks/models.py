# tasks/models.py
# Models represent database tables. Django ORM handles SQL for us.

from django.db import models
from django.contrib.auth.models import User  # Built-in User model for auth.

class Task(models.Model):
    # Choices for priority: Defines fixed options.
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)  # Short text field for task title.
    description = models.TextField(blank=True)  # Longer text, optional.
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')  # Priority level.
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  # Link to User; delete tasks if user deleted.
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set on creation.
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update on save.
    due_date = models.DateTimeField(null=True, blank=True)  # Optional due date for reminders.
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title  # Human-readable representation.