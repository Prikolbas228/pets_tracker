
from django.contrib.auth.models import User
from django.db import models



#PETS
class Pet(models.Model):
    SPECIES = [('dog','Собака'),('cat','Кошка'),('bird','Птица'),('other','Другое')]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(choices=SPECIES)
    photo = models.ImageField(upload_to='pets/', blank=True)
    birth_date = models.DateField()

# habits
class HabitLog(models.Model):
    CATEGORY = [
        ('feeding','Кормление'), ('walk','Прогулка'),
        ('vet','Ветеринар'), ('medicine','Лекарства'),
        ('weight','Вес'), ('grooming','Груминг'),
    ]
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='logs')
    category = models.CharField(choices=CATEGORY)
    notes = models.TextField(blank=True)
    logged_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True)  # для расписания
#REMINDERS
class Reminder(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    category = models.CharField(choices=HabitLog.CATEGORY)
    message = models.CharField(max_length=255,blank=True, default='')
    remind_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)