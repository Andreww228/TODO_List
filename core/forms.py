from django import forms

from core.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = '__all__'
