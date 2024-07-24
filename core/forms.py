from django import forms

from core.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags"
        ]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
