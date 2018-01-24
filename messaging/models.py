from django.db import models
from datetime import datetime


class MessageManager(models.Manager):
    def create_message(self, content):
        message = self.create(content=content,
                              author="default")
        return message


class Message(models.Model):
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=datetime.now)

    objects = MessageManager()

    def __str__(self):
        return self.content


# class Question(Message):


class Answer(Message):
    parent = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='answers')


