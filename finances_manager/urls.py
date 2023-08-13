from django.contrib import admin
from django.urls import path, include
import transactions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transactions.urls')),
]