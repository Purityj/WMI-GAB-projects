from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mentor/', views.mentor, name='mentor'),
    path('mentee/', views.mentee, name='mentee'),
]