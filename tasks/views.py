from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm, CustomUserCreationForm

# Create your views here.
def home(request):
  if request.user.is_authenticated:
    return redirect('tasks:task_list')
  return render(request, 'tasks/home.html')

@login_required
def task_list(request):
  all_tasks = Task.objects.filter(user=request.user)

  overdue_tasks = Task.objects.overdue(request.user)

  context = {
    'all_tasks': all_tasks,
    'overdue_tasks': overdue_tasks
  }

  return render(request, 'tasks/task_list.html', context)

@login_required
def task_create(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      task = form.save(commit=False)
      task.user = request.user
      task.save()
      return redirect('tasks:task_list')
  else:
    form = TaskForm()

  context = {
    'form': form,
    'title': 'Create new Task'
  }

  return render(request, 'tasks/task_form.html', context)

@login_required
def task_edit(request, pk):
  task = get_object_or_404(Task, pk=pk, user=request.user)

  if request.method == "POST":
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
      form.save()
      return redirect('tasks:task_list')
  else:
    form = TaskForm(instance=task)

  context = {
    'form': form,
    'title': f"Edit Task: {task.title}"
  }

  return render(request, 'tasks/task_form.html', context)

@login_required
def task_delete(request, pk):
  task = get_object_or_404(Task, pk=pk, user=request.user)

  if request.method == "POST":
    task.delete()
    return redirect('tasks:task_list')
  
  context = {
    'task': task,
    'title': f"Confirm Delete: {task.title}"
  }

  return render(request, 'tasks/task_confirm_delete.html', context)

def register(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('tasks:task_list')
  else:
    form = CustomUserCreationForm()

  context = {
    'form': form,
    'title': "Register"
  }

  return render(request, 'tasks/register.html', context)