from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# SCREEN 1: LIST - Ella task um
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'adm/task_list.html', {'tasks': tasks})

# SCREEN 2: ADD - Task add panna
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'adm/task_form.html', {'form': form, 'title': 'Add New Task'})

# SCREEN 3: EDIT / UPDATE - Task ah maathura
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'adm/task_form.html', {'form': form, 'title': 'Update Task'})

# DELETE
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')