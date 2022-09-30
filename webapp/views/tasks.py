from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, StateChoices
from webapp.forms import TaskForm


def add_view(request):
    form = TaskForm()
    if request.method == 'GET':
        return render(request, 'task_add.html', context={'choices': StateChoices.choices, 'form': form})
    form = TaskForm(request.POST)
    if not form.is_valid():
        print(form.errors)
        return render(request, 'task_add.html', context={'choices': StateChoices.choices, 'form': form})
    task = Task.objects.create(**form.cleaned_data)
    return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'to_do_list.html', context={'task': task})


def update_view(request, pk):
    errors = {}
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        if request.POST.get('name'):
            errors['name']: "The field is required"
        task.name = request.POST.get('name')
        task.state = request.POST.get('state')
        task.due_date = request.POST.get('due_date')
        task.description = request.POST.get('description')
        if errors:
            return render(
                request,
                'task_update.html',
                context={
                    'task': task,
                    'choices': StateChoices.choices,
                    'errors': errors
                })
        task.save()
        return redirect('task_detail', pk=task.pk)
    return render(
        request,
        'task_update.html',
        context={
            'task': task,
            'choices': StateChoices.choices,
        })


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
