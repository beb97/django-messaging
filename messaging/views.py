from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Message


def index(request):
    latest_messages = Message.objects.order_by('creation_date')[:5]
    context = {
        'latest_messages': latest_messages,
    }
    return render(request, 'messaging/index.html', context)
    # return HttpResponse(template.render(context, request))


def detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'messaging/detail.html', {'message': message})


def results(request, message_id):
    response = "Reponses : %s"
    return HttpResponse(response % message_id)


def answer(request, message_id):
    return HttpResponse("Answering : %s" % message_id)
