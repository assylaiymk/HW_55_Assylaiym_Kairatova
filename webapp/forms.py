from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name')
    state = forms.CharField(max_length=10, required=True, label='State')
    due_date = forms.CharField(max_length=2000,
                               required=True,
                               label='Due_date',
                                widget=widgets.Textarea)
