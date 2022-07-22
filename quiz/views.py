from django.http import JsonResponse
from django.shortcuts import render
from .models import Menti,Player,Question

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    username = request.GET['username']
    room_name = request.GET['room']
    room_name_present = Menti.objects.filter(room = room_name).first()
    if room_name_present :
        Player.objects.get_or_create(username = username,room = room_name_present)
        ctx = {"username":username,"room_name":room_name}
        return render(request,'menti.html',ctx)
    else :
        ctx = {"error":"Invalid room name."}
        return render(request,'index.html',ctx)


def get_question_count(request , room_name):
    data = {}
    room = Menti.objects.filter(room = room_name).first()
    question_count = Question.objects.filter(room=room).count()
    data["question_count"]=question_count
    return JsonResponse(data,safe=False)


def get_questions(request,room_name,index):
    pass

