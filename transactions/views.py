from django.shortcuts import render
from django.http import JsonResponse

from models import Income, Expense

def index(request):
    return render(request, 'index.html')

def get_incomes(request):
    incomes = Income.objects.all()
    data = [{'description': income.description, 'amount': income.amount, 'date': income.date} for income in incomes]
    return JsonResponse(data, safe=False)

def get_expenses(request):
    expenses = Expense.objects.all()
    data = [{'description': expense.description, 'amount': expense.amount, 'date': expense.date} for expense in expenses]
    return JsonResponse(data, safe=False)
