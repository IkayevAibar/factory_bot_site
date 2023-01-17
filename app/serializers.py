from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import User, Bot, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name']

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'first_name', 'password', )

class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ['id', 'token','chat_id']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user','bot','message_body','sended_at']

# class BotCreateSerializer(serializers.ModelSerializer):
#     # def create(self, validated_data):
#     #     instance, _ = Bot.objects.get_or_create(**validated_data)
#     #     return instance

#     class Meta:
#         model = Bot
#         fields = ['token','chat_id']
