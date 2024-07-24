from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from core.models import Task


class HomePageView(TemplateView):
    template_name = 'base.html'


class TaskListView(generic.ListView):
    template_name = "core/task-list.html"

    def get_queryset(self):
        queryset = Task.objects.all()

        queryset = queryset.order_by("is_done").order_by("created_date")
        return queryset

