from django.urls import path

from core.views import (HomePageView,
                        CreateTaskView,
                        CreateTagView, TagListView, UpdateTagView, DeleteTagView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("create-task", CreateTaskView.as_view(), name='create-task'),
    path("create-tag", CreateTagView.as_view(), name='create-tag'),
    path("tags/", TagListView.as_view(), name='tags'),
    path("tags/update/<int:pk>", UpdateTagView.as_view(), name='update-tag'),
    path("tags/delete/<int:pk>", DeleteTagView.as_view(), name='delete-tag'),

]

app_name = 'core'