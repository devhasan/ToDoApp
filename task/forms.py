from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Task


class CreateTask(forms.ModelForm):
    class Meta:
         model = Task
         fields = ['title','description', 'date','time', 'category', 'priority', 'assigned_to']
         widgets = {
             'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Task title', 'required':True}),
             'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Task description', 'required':True}),
             'date': forms.DateInput(attrs={'type':'date', 'class':'form-control', 'placeholder':'Date', 'required':True, 'autofocus':True}),
             'time': forms.TimeInput(attrs={'type':'time','class':'form-control', 'placeholder':'Time', 'required':True}),
             'category': forms.Select(attrs={'class':'form-select', 'placeholder':'Category', 'required':True}),
             'priority': forms.Select(attrs={'class':'form-select', 'placeholder':'Priority', 'required':True}),
             'assigned_to': forms.Select(attrs={'class':'form-select', 'placeholder':'Assign To', 'required':True}),
           }
    
