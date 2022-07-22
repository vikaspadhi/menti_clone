from django.urls import path,include
from .views import index,register , get_question_count
urlpatterns = [
    path('', index),
    path('menti/',register),
    path('question_count/<str:room_name>/',get_question_count)
]