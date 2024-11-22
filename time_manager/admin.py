from django.contrib import admin
from .models import Task, Event

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'completed')
    list_filter = ('completed', 'due_date', 'user')
    search_fields = ('title', 'description')
    ordering = ()
    date_hierarchy = 'due_date'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_time', 'end_time')
    list_filter = ('user', 'start_time')
    search_fields = ('title', 'description')
    ordering = ('-start_time',)
    date_hierarchy = 'start_time'
