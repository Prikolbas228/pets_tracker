from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pet, HabitLog, Reminder


# === ACCOUNTS ===
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# === PETS ===
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'photo', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


# === HABITS ===
class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['category', 'notes', 'scheduled_at']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'scheduled_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['category', 'message', 'remind_at']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'remind_at': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }