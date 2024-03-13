from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('current_day/', views.current_day_of_week, name='current_day'),
]