from django.urls import path

from core.views import (HomePageView,
                        CreateTaskView,
                        CreateTagView, TagListView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("create-task", CreateTaskView.as_view(), name='create-task'),
    path("create-tag", CreateTagView.as_view(), name='create-tag'),
    path("tags/", TagListView.as_view(), name='tags'),
]

app_name = 'core'