from django.urls import path
from .views  import product_list, product_detail, reg, login, payment


urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('register/', reg, name='register'),
    path('login/', login, name='login'),
    path('product/<int:pk>/payment', payment, name='payment')
    # path('main/', views.main, name='main'),
    # path('main/details/<int:id>', views.details, name='details'),
]