from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def addTask(request):
    task = request.POST['task']                                                                                         #from the add button
    Task.objects.create(task=task)                                                                                      #based on the models
    return redirect ('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task,pk=pk)                                                                                #fetching the object from database if it exists
    task.is_completed=True
    task.save()
    return redirect ('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task,pk=pk)                                                                                #fetching the object from database if it exists
    task.is_completed=False
    task.save()
    return redirect ('home')

def edit_task(request,pk):
    get_task = get_object_or_404(Task, pk=pk)                                                                           #fetching the object from database if it exists
    if request.method =='POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task':get_task,
        }
        return render(request,'edit_task.html', context)

def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)                                                                                #fetching the object from database if it exists
    task.delete()                                                                                                       #deleting the object based on a pk
    return redirect('home')
