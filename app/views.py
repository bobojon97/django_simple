from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(requets):
    tasks = Task.objects.all()
    return render (requets, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(requets):
    return render (requets, 'main/about.html')
    

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render (request, 'main/create.html', context)
    