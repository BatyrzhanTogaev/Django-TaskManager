from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


def render_view(request, extra_context=None):
    '''
    Функция, которая рендерить шаблон с формами и задачами пользователя
    '''
    tasks = Task.objects.filter(author=request.user)
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    if extra_context:
        context.update(extra_context)

    return render(request, 'main/HomePage.html', context)


def home_page_view(request):
    return render_view(request)


@login_required
def create_task_view(request):
    '''
    Функция для создания задачи
    '''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.author = request.user
            task.save()

    else:
        form = TaskForm()
    return redirect('HomePage')


@login_required
def delete_task_view(request, pk):
    '''
    Функция для удаления задачи
    '''
    task = get_object_or_404(Task, pk=pk, author=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('HomePage')


@login_required
def edit_task_view(request, pk):
    '''
    Функция которая принимает GET запрос
    И переотправляет на POST запрос
    '''
    task = get_object_or_404(Task, pk=pk, author=request.user)
    return render_view(request, {'edit_task': task})


@login_required
def update_task_view(request, pk):
    '''
    Функция которая отправляет форму для редактирования задач
    '''
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    return render_view(request, {'edit_task': task, 'form': form})
