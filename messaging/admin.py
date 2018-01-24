from django.contrib import admin

from .models import Message
from .models import Answer

# Register your models here.
admin.site.register(Message)
admin.site.register(Answer)
