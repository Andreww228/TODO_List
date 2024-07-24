from django.urls import path

from core import views
from core.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

app_name = 'core'