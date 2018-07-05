from django.shortcuts import render
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'helpseeking/task_list.html', {'tasks': tasks})