from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('remove_activity/<int:activity_id>/', views.remove_activity, name='remove_activity'),
    path('register_activity/<int:activity_id>/', views.register_activity, name='register_activity'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('activity_list/', views.activity_list, name='activity_list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
