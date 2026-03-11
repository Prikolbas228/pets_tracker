from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # accounts
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),

    # pets
    path('', views.pet_list, name='pet_list'),
    path('pets/add/', views.pet_add, name='pet_add'),
    path('pets/<int:pk>/', views.pet_detail, name='pet_detail'),

    # habits
    path('pets/<int:pet_pk>/habit/add/', views.habit_add, name='habit_add'),
    #notification
    path('reminders/', views.reminder_list, name='reminder_list'),
    path('pets/<int:pet_pk>/reminder/add/', views.reminder_add, name='reminder_add'),
    path('pets/<int:pet_pk>/delete/', views.remove_pet, name='remove_pet'),
    path('logs/<int:log_pk>/delete/', views.remove_log, name='remove_log'),
    path('reminders/<int:reminder_pk>/delete/', views.remove_reminder, name='remove_reminder'),
]