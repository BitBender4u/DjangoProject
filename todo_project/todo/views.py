from django.shortcuts import render, redirect
from.models import Task
from .Forms import TaskForm

# Create your views here.
# A method to list our task, create a task
# Method to list task
def task_list(request):
    # All the records in our dbs
    #rows : represents the objects
    tasks = Task.objects.all()
    return render(request,  'todo/task_list.html',  {'tasks': tasks})

def task_create(request):

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'todo/task_form.html', {'form': form})
