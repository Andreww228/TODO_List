from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views import generic

from core.forms import TaskForm, TagForm
from core.models import Task, Tag


class HomePageView(generic.ListView):
    template_name = "core/task-list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = Task.objects.prefetch_related().all()

        queryset = queryset.order_by("is_done").order_by("create_date")
        return queryset


class UpdateTaskView(generic.edit.UpdateView):
    form_class = TaskForm
    success_url = "/"
    model = Task
    template_name = "core/task-form.html"


class DeleteTaskView(generic.edit.DeleteView):
    model = Task
    success_url = "/"

    def get(self, *args, **kwargs):
        task = self.get_object()
        if task:
            task.delete()
        return redirect(self.success_url)


class TagListView(generic.ListView):
    template_name = "core/tag-list.html"
    model = Tag
    paginate_by = 10


class CreateTagView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = "/tags/"
    template_name = "core/tag-form.html"


class UpdateTagView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = "/tags/"
    template_name = "core/tag-form.html"


class DeleteTagView(generic.DeleteView):
    model = Tag
    success_url = "/tags/"

    def get(self, *args, **kwargs) -> HttpResponse:
        tag = self.get_object()
        if tag:
            tag.delete()
        return redirect(self.success_url)


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = "/"
    template_name = "core/task-form.html"


def change_task_status_view(request, pk):
    if not pk:
        raise Http404
    task_query = Task.objects.filter(pk=pk)
    if not task_query.exists():
        raise Http404
    task = task_query.first()
    if task:
        task.is_done = not task.is_done
        task.save()
    return redirect("/")

