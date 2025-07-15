from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task

    fields = ['title', 'description', 'due_date', 'priority', 'is_complete']

    widgets = {
      'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
      'description': forms.Textarea(attrs={'rows': 4})
    }

    labels = {
      'is_complete': 'Mark as Complete'
    }

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('email',)