from django.shortcuts import render, redirect

# Create your views here.
from Todo.forms import TodoForm
from Todo.models import Todo


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, "Todo/index.html", context)


def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, "Todo/index.html", {'form': form})


def complete(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save();
    return redirect('index')


def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Todo/update.html', {'form': form})


def delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'Todo/delete.html', {'todo': todo})
