from django.urls import path
from transactions import views

urlpatterns = [
    path('incomes/', views.income_list, name='income-list'),
    path('incomes/<int:pk>/', views.income_detail, name='income-detail'),
    path('expenses/', views.expense_list, name='expense-list'),
    path('expenses/<int:pk>/', views.expense_detail, name='expense-detail'),
    path('goals/', views.goal_list, name='goal-list'),
    path('goals/<int:pk>/', views.goal_detail, name='goal-detail'),
]
