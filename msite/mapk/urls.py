from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('details/', views.details, name='details')
]