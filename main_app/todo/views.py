from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def addTask(request):
    task = request.POST['task']                                                                                         #from the button
    Task.objects.create(task=task)                                                                                               #based on the models
    return redirect ('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task,pk=pk)                                                                                #fetching the object from database if it exists
    task.is_completed=True
    task.save()
    return redirect ('home')