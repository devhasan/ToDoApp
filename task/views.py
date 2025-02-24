from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Task
from django.db.models import Q
from .forms import CreateTask

# Create your views here.
@login_required
def home(request):
    #user = request.user
    tasks = Task.objects.filter(Q(user=request.user) | Q(assigned_to=request.user)).order_by('-created_at')
    return render(request, 'task/home.html', {'tasks': tasks})

@login_required
def createtask(request):
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = CreateTask()
    return render(request, 'task/createtask.html', {'form':form})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateTask(instance=task)
    return render(request, 'task/createtask.html', {'form': form})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('home')