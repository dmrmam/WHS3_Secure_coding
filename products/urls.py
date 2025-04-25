from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/purchase/', views.request_purchase, name='request_purchase'),
    path('purchase/<int:purchase_id>/accept/', views.accept_purchase, name='accept_purchase'),
]