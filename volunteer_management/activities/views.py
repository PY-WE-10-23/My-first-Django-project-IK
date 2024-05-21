from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ActivityForm, RegistrationForm
from .models import Activity, Registration

def index(request):
    return render(request, 'activities/index.html')

@login_required
def add_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm()
    return render(request, 'activities/add_activity.html', {'form': form})

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activities/edit_activity.html', {'form': form, 'activity': activity})

@login_required
def remove_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == "POST":
        activity.delete()
        return redirect('activity_list')
    return render(request, 'activities/remove_activity.html', {'activity': activity})

@login_required
def register_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.activity = activity
            registration.user = request.user
            registration.save()
            return redirect('activity_list')
    else:
        form = RegistrationForm()
    return render(request, 'activities/register_activity.html', {'form': form, 'activity': activity})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'activities/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'activities/register.html', {'form': form})

def activity_list(request):
    activities = Activity.objects.all()
    for activity in activities:
        activity.remaining_slots = activity.available_slots - activity.registration_set.count()
    return render(request, 'activities/activity_list.html', {'activities': activities})

def privacy_policy(request):
    return render(request, 'activities/privacy_policy.html')
