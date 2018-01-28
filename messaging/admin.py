from django.contrib import admin

from .models import Message, Answer, Question

# Register your models here.
admin.site.register(Message)
admin.site.register(Answer)
admin.site.register(Question)
