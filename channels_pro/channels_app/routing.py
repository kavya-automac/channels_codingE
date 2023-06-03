from django.urls import path
# from. import consumers
from .consumers import *



print("routingggg")
websocket_urlpatterns=[
    path('test/',TestConsumer.as_asgi()),

]