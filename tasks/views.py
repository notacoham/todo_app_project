from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.


@login_required
def task_list(request):
  tasks = Task.objects.filter(user=request.user)

  overdue_tasks = Task.objects.overdue(request.user)

  context = {
    'tasks': tasks,
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