from django import forms
from django.utils import timezone

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

    def clean(self):
        cleaned_date = super().clean()
        deadline = cleaned_date.get("deadline", None)
        if not deadline:
            return cleaned_date
        if deadline <= timezone.now():
            raise forms.ValidationError(
                {
                    "deadline": "Deadline cannot be in the past"
                }
            )
        return cleaned_date


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
