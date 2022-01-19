from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home')
]