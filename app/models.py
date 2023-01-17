from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import UserManager

# Create your models here.
class User(AbstractUser):
    email = None 
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return "%d.%s" % (self.id, self.username)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Bot(models.Model):
    token = models.ForeignKey(Token, verbose_name="Токен юзера", on_delete=models.CASCADE)
    chat_id = models.CharField(_("Индетификатор чата в tg"), max_length=200, null=True, blank=True)
    
    class Meta:
        unique_together = ('token', 'chat_id',)

class Message(models.Model):
    user = models.ForeignKey(User, verbose_name="Отправитель сообщения", on_delete=models.CASCADE)
    bot = models.ForeignKey(Bot, verbose_name="Получатель[Bot] сообщения", on_delete=models.CASCADE)
    message_body = models.TextField(_("Сообщение"), max_length=500, null=True, blank=True)

# Token.add_to_class('last_request', models.DateTimeField("Last request made by user", null=True, blank=True))
