from django.db import models
from dotenv import load_dotenv
import os

load_dotenv()


# Create your models here.

class QuestFeedBack(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    PARA = '2'
    NOT_PARA = '1'
    CANT = '0'
    ANSWER = [
        (PARA, 'Со второй половинкой'),
        (NOT_PARA, 'Один/Одна'),
        (CANT, 'Не получится придти'),
    ]
    para = models.CharField(max_length=1, choices=ANSWER, default=NOT_PARA)

    def __str__(self):
        if self.para == self.NOT_PARA:
            return f'Гость: {self.name} {self.name}. Придет без второй половинки'
        elif self.para == self.PARA:
            return f'Гость: {self.name} {self.name}. Придет со второй половинкой'
        else:
            return f'Гость не сможет придти'


class AuthModel(models.Model):
    SECRET_QUEST_PASSWORD = os.getenv('SECRET_QUEST_PASSWORD')
    field = models.CharField(max_length=10, default='passwod')
