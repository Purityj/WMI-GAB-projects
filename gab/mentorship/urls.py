from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mentor/', views.mentor, name='mentor'),
    path('mentee/', views.mentee, name='mentee'),
    path('analytics/', views.analytics, name='analytics'),
    path('analytics-data/', views.demographics_data_api, name='analytics-data'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
