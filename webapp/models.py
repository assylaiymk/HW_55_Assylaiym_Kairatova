from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StateChoices(TextChoices):
    NEW = 'NEW', 'New'
    EXISTS = 'EXISTS', 'Exists'


class Task(models.Model):
    name = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Text', max_length=3000, null=False, blank=False, default='No task')
    state = models.CharField(verbose_name='State', choices=StateChoices.choices, max_length=100,
                             default=StateChoices.NEW)
    due_date = models.DateTimeField(verbose_name='Due date', max_length=100)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)

    def __str__(self):
        return f'{self.name} - {self.due_date}'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
