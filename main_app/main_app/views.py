from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False). order_by('-updated_at')                                            #grabbing the tasks that are have not been completed
                                                                                                                        #in the descending updated_at order
    completed_tasks = Task.objects.filter(is_completed=True)
    context = {                                                                                                         #filter will grab all, get only one
        'tasks':tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request,'home.html', context)