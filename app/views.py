from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.authtoken.models import Token

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import User, Bot
from .serializers import UserSerializer, UserRegistrationSerializer, BotSerializer, MessageSerializer

import requests
# from todo import serializers

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer
    
    def get_queryset(self):
        return self.queryset

def api_tg_call(bot:Bot, user:User ,text):
    message_text = user.first_name+", я получил от тебя сообщение:\n"+text
    payload = dict(text=message_text,chat_id=bot.chat_id)

    # так как у нас только один бот пока сделаю так, если бы было больше ботов то можно это всё проапдейтить
    r = requests.api.post("https://api.telegram.org/bot5804287527:AAHS5NpknvEmZPqWYsgnB08Xk5XtvNlaR9I/sendMessage",data=payload)
    
    if(r.status_code == 200):
        return Response(r.json, status=status.HTTP_200_OK)
    return Response(r.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def send_message_to_chat(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        api_tg_call(Bot.objects.get(id=request.data["bot"]), User.objects.get(id=request.data["user"]), request.data["message_body"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or created.
    """
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # def get_serializer_class(self):
    #         if self.action == 'create':
    #             return BotCreateSerializer
    #         return BotSerializer

    def get_queryset(self):
        return self.queryset
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
 