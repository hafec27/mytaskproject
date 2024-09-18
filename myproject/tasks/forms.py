# forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'completed','note']
        
    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
