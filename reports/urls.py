from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),  # ✅ 추가
    path('product/<int:product_id>/', views.report_product, name='report_product'),
    path('user/<int:user_id>/', views.report_user, name='report_user'),
    path('list/', views.report_list, name='report_list'),  # 이미 있던 거
]