from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('activities/', views.activity_list, name='activity_list'),
    path('register_activity/<int:activity_id>/', views.register_activity, name='register_activity'),
    path('remove_activity/<int:activity_id>/', views.remove_activity, name='remove_activity'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
