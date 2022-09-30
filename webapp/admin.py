from django.contrib import admin

from webapp.models import Task


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'due_date', 'created_at')
    list_filter = ('id', 'name', 'state', 'due_date', 'created_at')
    search_fields = ('name', 'due_date')
    fields = ('name', 'state', 'due_date', 'created_at', 'changed_at')
    readonly_fields = ('id', 'created_at', 'changed_at')


admin.site.register(Task, TasksAdmin)
