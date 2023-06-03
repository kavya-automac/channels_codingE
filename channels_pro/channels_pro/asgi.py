"""
ASGI config for channels_pro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from channels_app import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_pro.settings')



print('asgi')





application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(
        routing.websocket_urlpatterns
    ))
})


