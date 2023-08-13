from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/incomes/', views.get_incomes, name='get_incomes'),
    path('api/expenses/', views.get_expenses, name='get_expenses'),
]
