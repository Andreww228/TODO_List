from django import forms

from core.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
