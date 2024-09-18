from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

# タスクリスト表示
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# 新しいタスク追加
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # `due_date` が空の場合は None を設定
            if form.cleaned_data['due_date'] == '':
                task.due_date = None
            else:
                task.due_date = form.cleaned_data['due_date']
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


# 完了状態
def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # 完了/未完了切り替え
    task.save()
    return redirect('task_list')

# タスクの編集
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            # `due_date` が空の場合に None を設定する
            if form.cleaned_data['due_date'] == '':
                task.due_date = None
            else:
                task.due_date = form.cleaned_data['due_date']
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})


# タスクを削除
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

