from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Task

def home(request):
    context = {'success' : False, 'name' : 'Swayam  '}
    if request.method == "POST":
        desc = request.POST['desc']
        title = request.POST['title']
        instance = Task(task_title=title, task_desc=desc)
        instance.save()
        context['success'] = True

    return render(request, 'index.html', context=context)

def tasks(request):
    allTask = Task.objects.all()
    context = {'tasks' : allTask}
    return render(request, 'tasks.html', context = context)


def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    allTask = Task.objects.all()
    context = {'tasks' : allTask}
    return render(request, 'tasks.html', context = context)

