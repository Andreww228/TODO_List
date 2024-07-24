from django.urls import path

from core.views import (HomePageView,
                        CreateTaskView,
                        CreateTagView,
                        TagListView,
                        UpdateTagView,
                        DeleteTagView,
                        UpdateTaskView,
                        DeleteTaskView,
                        change_task_status_view)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("create-task", CreateTaskView.as_view(), name='create-task'),
    path("task/update/<int:pk>", UpdateTaskView.as_view(), name='update-task'),
    path("task/update-status/<int:pk>", change_task_status_view, name='update-task-status'),
    path("task/delete/<int:pk>", DeleteTaskView.as_view(), name='delete-task'),
    path("create-tag", CreateTagView.as_view(), name='create-tag'),
    path("tags/", TagListView.as_view(), name='tags'),
    path("tags/update/<int:pk>", UpdateTagView.as_view(), name='update-tag'),
    path("tags/delete/<int:pk>", DeleteTagView.as_view(), name='delete-tag'),
]

app_name = 'core'