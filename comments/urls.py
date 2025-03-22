from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comments/', views.comments, name='comments'),
]