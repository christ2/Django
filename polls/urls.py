from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index_view, name='indexing'),
    path('profile/', views.profile_view, name='profile'),
    path('chatroom/', views.chatroom, name='chat_room'),
    path('lockscreen/', views.lockscreen, name='lock_screen'),
    path('unlock/', views.unlock, name='unlock'),
    path('newsegment/', views.createsegment, name='newsegment'),
    # path('polls/', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]