from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import logout, login
from django.views.decorators.http import require_http_methods
from .models import Task, Event
from .forms import TaskForm, EventForm, UserRegistrationForm

@login_required
def dashboard(request):
    print(f"Current user: {request.user}")
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    events = Event.objects.filter(user=request.user).order_by('start_time')
    return render(request, 'time_manager/dashboard.html', {'tasks': tasks, 'events': events})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'time_manager/task_list.html', {'tasks': tasks})


@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user).order_by('start_time')
    return render(request, 'time_manager/event_list.html', {'events': events})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'time_manager/task_form.html', {'form': form})


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_at = timezone.now() 
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/add.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'time_manager/task_form.html', {'form': form, 'task': task})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'time_manager/event_form.html', {'form': form, 'event': event})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if not task.completed:
        task.completed = True
        task.save()
    return redirect('task_list')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('event_list')


@require_http_methods(["GET", "POST"])
def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'time_manager/logout_confirmation.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'time_manager/register.html', {'form': form})

