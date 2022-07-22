import json
from tokenize import group
from channels.consumer import SyncConsumer
from . models import Menti , Question , Answer
from django.db.models import F
from asgiref.sync import async_to_sync

class MyConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("WS Connected...")
        # getting room name
        self.grp_name = self.scope['url_route']['kwargs']['roomname']
        # updating active user count
        Menti.objects.filter(room=self.grp_name).update(users_joined= F('users_joined')+1)
        # adding channel into the group
        async_to_sync(self.channel_layer.group_add)(self.grp_name,self.channel_name)
        # getting number of active users
        obj = Menti.objects.get(room = self.grp_name)
        data = {"users_joined":obj.users_joined}
        async_to_sync(self.channel_layer.group_send)(self.grp_name,{
            'type':'chat.message',
            'message':json.dumps(data)
        })

        # accepting the connection
        self.send({'type':'websocket.accept'})

    def chat_message(self,event):
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })

    def websocket_receive(self,event):
        data = json.loads(event['text'])
        room_name = data['room_name']
        q_no = int(data['q_no'])
        menti = Menti.objects.filter(room=self.grp_name).first()
        question = Question.objects.filter(room=menti)[q_no]
        # print(question)
        options = Answer.objects.filter(question=question).values_list('answer','is_correct')
        # print(options)

        obj = Menti.objects.get(room = self.grp_name)

        ctx = {}
        ctx['question'] = question.question
        ctx['options'] = list(options)
        ctx["users_joined"]=obj.users_joined
        async_to_sync(self.channel_layer.group_send)(self.grp_name,{
            'type':'chat.message',
            'message':json.dumps(ctx)
        })
        
    def websocket_disconnect(self,event):
        print("WS disconnected...")
        Menti.objects.filter(room=self.grp_name).update(users_joined= F('users_joined')-1)
        async_to_sync(self.channel_layer.group_discard)(self.grp_name, self.channel_name)
        obj = Menti.objects.get(room = self.grp_name)
        data = {"users_joined":obj.users_joined}
        async_to_sync(self.channel_layer.group_send)(self.grp_name,{
            'type':'chat.message',
            'message':json.dumps(data)
        })