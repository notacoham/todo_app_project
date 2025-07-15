from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

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