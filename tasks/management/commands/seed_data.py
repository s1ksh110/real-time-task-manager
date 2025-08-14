# tasks/management/commands/seed_data.py
# Custom command to add dummy data.

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task

class Command(BaseCommand):
    help = 'Seeds the database with dummy data'

    def handle(self, *args, **kwargs):
        user, _ = User.objects.get_or_create(username='demo', email='demo@example.com')
        user.set_password('password')
        user.save()

        Task.objects.create(title='Task 1', description='Low prio', priority='low', assigned_to=user)
        Task.objects.create(title='Task 2', description='High prio', priority='high', assigned_to=user)
        self.stdout.write(self.style.SUCCESS('Dummy data seeded'))