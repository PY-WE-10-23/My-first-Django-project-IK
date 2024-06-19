from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Activity, Registration
from .forms import UserRegistrationForm, ActivityForm, RegistrationForm, LoginForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'activities/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'activities/register.html', {'form': form})

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ActivityForm()
    return render(request, 'activities/add_activity.html', {'form': form})

def activity_list(request):
    activities = Activity.objects.all()
    registrations = Registration.objects.select_related('user', 'activity').all()
    activity_registrations = {}
    for registration in registrations:
        if registration.activity.id not in activity_registrations:
            activity_registrations[registration.activity.id] = []
        activity_registrations[registration.activity.id].append(registration.user)


    # Filtry
    user_id = request.GET.get('user_id')
    if user_id:
        activities = activities.filter(registration__user_id=user_id)
        print(activities)

    date_sort = request.GET.get('date_sort')
    if date_sort == 'asc':
        activities = activities.order_by('date')
    elif date_sort == 'desc':
        activities = activities.order_by('-date')

    slots_sort = request.GET.get('slots_sort')
    if slots_sort == 'asc':
        activities = activities.order_by('available_slots')
    elif slots_sort == 'desc':
        activities = activities.order_by('-available_slots')

    total_slots = request.GET.get('total_slots')
    if total_slots:
        activities = activities.filter(available_slots__gte=int(total_slots))

    # Přidání dostupných slotů do aktivit

    for activity in activities:
            activity.registered_count = len(activity_registrations.get(activity.id, []))
            activity.available_count = activity.available_slots - activity.registered_count

    context = {
        'activities': activities,
        'activity_registrations': activity_registrations,
        'user_list': User.objects.all()
    }

    return render(request, 'activities/activity_list.html', context)

def register_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.activity = activity
            registration.save()
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'activities/register_activity.html', {'form': form, 'activity': activity})

@login_required
def remove_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity_list')
    return render(request, 'activities/remove_activity.html', {'activity': activity})

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list')
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activities/edit_activity.html', {'form': form, 'activity': activity})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'activities/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def privacy_policy(request):
    return render(request, 'activities/privacy_policy.html')

def about(request):
    return render(request, 'activities/about.html')