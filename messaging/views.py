from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question


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
    Question.objects.create(content=request.POST.get('question'),
                            title=request.POST.get('title'))
    return redirect('messaging:index')


@login_required
def answer(request, question_id):
    answered_question = get_object_or_404(Question, pk=question_id)
    answered_question.answers.create_message(request.POST.get('answer'))
    return redirect('messaging:detail', question_id=question_id)


def search(request):
    search_term = request.GET.get('search')
    questions_list = []
    if search_term:
        questions_list = Question.objects.filter(title__contains=search_term).order_by('creation_date')[:5]
    context = {
        'questions_list': questions_list,
    }
    return render(request, 'messaging/search.html', context)
