from django.contrib import admin
from django.urls import path
from .views import clanbattlemain

urlpatterns = [
    path('', clanbattlemain, name='clanbattle'),
]