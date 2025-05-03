from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def home_page_view(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, 'main/HomePage.html', {'tasks': tasks, 'form': form})


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
