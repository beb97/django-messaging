from django.db import models
from django.utils import timezone


class MessageManager(models.Manager):
    def create_message(self, content):
        message = self.create(content=content,
                              author="default",
                              creation_date=timezone.now())
        return message


class Message(models.Model):
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now())

    objects = MessageManager()

    def __str__(self):
        return self.content


# class Question(Message):


class Answer(Message):


