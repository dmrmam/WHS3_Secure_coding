from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/ban/<int:user_id>/', views.ban_user, name='ban_user'),
    path('admin-dashboard/unban/<int:user_id>/', views.unban_user, name='unban_user'),
    path('admin-dashboard/delete/<int:user_id>/', views.delete_user, name='delete_user'),
]