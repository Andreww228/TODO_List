from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from core.forms import TaskForm, TagForm
from core.models import Task, Tag


class HomePageView(generic.ListView):
    template_name = "core/task-list.html"

    def get_queryset(self):
        queryset = Task.objects.all()

        queryset = queryset.order_by("is_done").order_by("create_date")
        return queryset


class TagListView(generic.ListView):
    template_name = "core/tag-list.html"
    model = Tag


class CreateTagView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = "/tags/"
    template_name = "core/tag-form.html"


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = "/"
    template_name = "core/create-task.html"
