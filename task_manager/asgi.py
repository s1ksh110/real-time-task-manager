"""
ASGI config for task_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

# Set Django settings before anything else imports models/settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Import after Django settings are configured
import tasks.routing  

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # HTTP requests
    'websocket': AuthMiddlewareStack(  # WebSockets with auth
        URLRouter(
            tasks.routing.websocket_urlpatterns
        )
    ),
})
