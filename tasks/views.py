from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from django.http import HttpResponse

# List all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Create a new task
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        category_id = request.POST.get('category')
        status = request.POST.get('status')
        category = Category.objects.get(id=category_id)

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            category=category,
        )
        return redirect('task_list')

    categories = Category.objects.all()
    return render(request, 'tasks/task_form.html', {'categories': categories})

# Edit an existing task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')
        task.category = Category.objects.get(id=request.POST.get('category'))

        task.save()
        return redirect('task_list')

    categories = Category.objects.all()
    return render(request, 'tasks/task_form.html', {'task': task, 'categories': categories})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
