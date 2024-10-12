from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    # path('main/', views.main, name='main'),
    # path('main/details/<int:id>', views.details, name='details'),
]