from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

# Overdue task manager class
class TaskManager(models.Manager):
  def overdue(self, user):
    return self.filter(user=user, is_complete=False, due_date__lt=timezone.now())
  
# Task Model
class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  due_date = models.DateTimeField(default=timezone.now)
  is_complete = models.BooleanField(default=False)

  PRIORITY_FIELD = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
  ]

  priority = models.CharField(max_length=10, choices=PRIORITY_FIELD, default='medium')

  objects = TaskManager()

class Meta:
  ordering = ['due_date', 'priority']

def __str__(self):
  return self.title
