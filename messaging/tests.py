from django.utils import timezone
# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from .models import Message, Question


class MessageModelTests(TestCase):

    def test_message_has_correct_fields(self):
        message = Message(content='hello')
        self.assertEqual(message.content, 'hello')
        self.assertEqual(message.author, 'no_author')
        self.assertEqual(message.creation_date.date(), timezone.now().date())


class QuestionModelTests(TestCase):

    def test_questions_without_answers_are_exculded(self):
        question = Question(content='mycontent', title='mytitle')
        question.save()
        self.assertEqual(len(Question.objects.all()), 1)
        self.assertEqual(len(Question.objects.get_answered_questions()), 0)
        question.answers.create(content="answer content")
        self.assertEqual(len(Question.objects.get_answered_questions()), 1)


class TestCalls(TestCase):

    def test_call_index(self):
        response = self.client.get('/messages/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/messages')
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/nomessages')
        self.assertEqual(response.status_code, 404)

    def test_index_messages(self):
        Question.objects.create(content='mycontent', title='mytitle1')
        Question.objects.create(content='mycontent', title='mytitle2')
        response = self.client.get(reverse('messaging:index'))
        self.assertQuerysetEqual(response.context['questions_list'],
                                 ['<Question: mytitle1>', '<Question: mytitle2>'])
