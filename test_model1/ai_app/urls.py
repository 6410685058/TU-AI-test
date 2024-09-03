from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_gemini, name='ai_gemini'),
]