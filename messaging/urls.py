from django.urls import path

from . import views

app_name = 'messaging'
urlpatterns = [
    # messages/
    path('', views.index, name='index'),
    # messages/1
    path('<int:message_id>/', views.detail, name='detail'),
    # messages/1/results/
    path('<int:message_id>/results/', views.results, name='results'),
    # messages/1/answer/
    path('<int:message_id>/answer', views.answer, name='answer'),
]
