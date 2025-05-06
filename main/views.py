from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


def render_view(request, extra_context=None):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    if extra_context:
        context.update(extra_context)

    return render(request, 'main/HomePage.html', context)


def home_page_view(request):
    return render_view(request)


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
    task = get_object_or_404(Task, pk=pk)
    return render_view(request, {'edit_task': task})


def update_task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    return render_view(request, {'edit_task': task, 'form': form})
