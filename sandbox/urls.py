
from django.urls import path
from . import views
app_name = "sandbox"

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list-url'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail-url'),
    path('thank-you/', views.thank_you, name='thank-you-url'),
    path('feedback/', views.feedback, name='feedback-url'),
]