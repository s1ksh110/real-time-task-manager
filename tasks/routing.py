# tasks/routing.py
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/tasks/$', __import__('tasks.consumers').consumers.TaskConsumer.as_asgi()),
]
