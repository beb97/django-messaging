from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView

from .models import Question
from django.contrib.auth.models import User


def index(request):
    questions_list = Question.objects.order_by('creation_date')[:5]
    context = {
        'questions_list': questions_list,
    }
    return render(request, 'messaging/index.html', context)


def detail(request, question_id):
    current_question = get_object_or_404(Question, pk=question_id)
    return render(request, 'messaging/detail.html', {'question': current_question})


def question(request):
    created_question = Question.objects.create(content=request.POST.get('question'),
                                               title=request.POST.get('title'),
                                               author=request.user)
    return redirect('messaging:detail', question_id=created_question.id)


@login_required
def answer(request, question_id):
    answered_question = get_object_or_404(Question, pk=question_id)
    answered_question.answers.create(content=request.POST.get('answer'),
                                     author=request.user)
    return redirect('messaging:detail', question_id=question_id)


def search(request):
    search_term = request.GET.get('search')
    questions_list = []
    if search_term:
        questions_list = Question.objects.get_answered_questions().filter(
            title__contains=search_term).order_by('creation_date')[:5]

    context = {
        'questions_list': questions_list,
    }
    return render(request, 'messaging/search.html', context)


class UserDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
