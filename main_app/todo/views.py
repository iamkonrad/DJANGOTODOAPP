from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']                                                                                         #from the button
    Task.objects.create(task=task)                                                                                               #based on the models
    return redirect ('home')