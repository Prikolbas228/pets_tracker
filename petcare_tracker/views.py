from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, PetForm, HabitLogForm, ReminderForm
from .models import Pet, HabitLog, Reminder
from django.utils import timezone



# === ACCOUNTS ===
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pet_add')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# === PETS ===
@login_required
def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)

    # считаем записи сегодня
    today = timezone.now().date()
    logs_today = HabitLog.objects.filter(
        pet__owner=request.user,
        logged_at__date=today
    ).count()

    # считаем напоминания
    reminders_count = Reminder.objects.filter(
        pet__owner=request.user,
        remind_at__gte=timezone.now(),
        is_sent=False
    ).count()

    return render(request, 'pets/pet_list.html', {
        'pets': pets,
        'logs_today': logs_today,
        'reminders_count': reminders_count,
    })


@login_required
def pet_add(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_add.html', {'form': form})

@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    logs = pet.logs.all().order_by('-logged_at')
    return render(request, 'pets/pet_detail.html', {'pet': pet, 'logs': logs})


# === HABITS ===
@login_required
def habit_add(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk, owner=request.user)
    if request.method == 'POST':
        form = HabitLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.pet = pet
            log.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = HabitLogForm()
    return render(request, 'habits/habit_add.html', {'form': form, 'pet': pet})
@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(
        pet__owner=request.user,
        is_sent=False
    ).order_by('remind_at')
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

@login_required
def reminder_add(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk, owner=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.pet = pet
            reminder.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = ReminderForm()
    return render(request, 'reminders/reminder_add.html', {'form': form, 'pet': pet})