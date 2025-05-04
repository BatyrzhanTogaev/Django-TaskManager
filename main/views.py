from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def home_page_view(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'main/HomePage.html', {
        'tasks': tasks, 'form': form
        })


def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.author = request.user
            task.save()

    else:
        form = TaskForm()

    return redirect('HomePage')


def delete_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('HomePage')
    

def edit_task_view(request, pk):
    edit_task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'main/HomePage.html', {
            'edit_task': edit_task
        })
