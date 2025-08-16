# tasks/tasks.py
# Celery tasks for background jobs.

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Task
from datetime import datetime, timedelta

@shared_task
def send_reminders():
    now = datetime.now()
    upcoming = Task.objects.filter(due_date__lte=now + timedelta(hours=1), due_date__gt=now)
    for task in upcoming:
        send_mail(
            'Task Reminder',
            f'Reminder: {task.title} is due soon.',
            settings.EMAIL_HOST_USER,  # Set in settings (use dummy for dev).
            [task.assigned_to.email],
            fail_silently=True,
        )
    return 'Reminders sent'