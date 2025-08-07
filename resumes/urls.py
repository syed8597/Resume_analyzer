from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_resume, name='upload_resume'),
    # path('chatbot/', views.career_chatbot, name='career_chatbot'),
    path('success/', views.resume_success, name='resume_success'),
]
