from django.urls import path
from . import consumers

websocket_urlpatterns =[
    path('ws/sc/<str:roomname>/',consumers.MyConsumer.as_asgi()),
]