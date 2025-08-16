# tasks/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'tasks'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Optional: Handle incoming messages if needed
        pass

    async def task_created(self, event):
        # Import here to avoid "Apps aren't loaded yet"
        from .models import Task
        from .serializers import TaskSerializer

        task = event['task']
        await self.send(text_data=json.dumps({'task': task}))
