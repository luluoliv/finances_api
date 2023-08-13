from django.urls import path
from transactions import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incomes/', views.IncomeList.as_view(), name='income-list'),
    path('incomes/<int:pk>/', views.IncomeDetail.as_view(), name='income-detail'),
    path('expenses/', views.ExpenseList.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view(), name='expense-detail'),
    path('goals/', views.GoalList.as_view(), name='goal-list'),
    path('goals/<int:pk>/', views.GoalDetail.as_view(), name='goal-detail'),
]
