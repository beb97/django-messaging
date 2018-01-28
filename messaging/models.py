from django.db import models
from django.utils import timezone


class MessageManager(models.Manager):
    def create_message(self, content):
        message = self.create(content=content)
        return message


class Message(models.Model):
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=100, default="no_author")
    creation_date = models.DateTimeField(default=timezone.now)

    objects = MessageManager()

    def __str__(self):
        return self.content


class QuestionManager(models.Manager):
    def get_answered_questions(self):
        questions = self.exclude(answers=None)
        return questions


class Question(Message):
    title = models.CharField(max_length=200)

    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(Message):
    parent = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')