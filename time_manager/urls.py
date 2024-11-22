from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('events/', views.event_list, name='event_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('events/add/', views.add_event, name='add_event'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('register/', views.register, name='register'),
]
