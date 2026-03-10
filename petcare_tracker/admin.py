from django.contrib import admin
from .models import Pet, HabitLog, Reminder

admin.site.register(Pet)
admin.site.register(HabitLog)
admin.site.register(Reminder)