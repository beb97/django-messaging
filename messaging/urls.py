from django.urls import path
from messaging.views import UserDetailView

from . import views

app_name = 'messaging'
urlpatterns = [
    # messages/
    path('', views.index, name='index'),
    # messages/1
    path('<int:question_id>/', views.detail, name='detail'),
    # messages/1/answer/
    path('<int:question_id>/answer', views.answer, name='answer'),
    path('question/', views.question, name='question'),
    path('search/', views.search, name='search'),
    path('profile/<int:pk>', UserDetailView.as_view(template_name="messaging/user_detail.html"), name='profile')
]
