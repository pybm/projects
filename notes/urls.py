from django.urls import path
from . import views

urlpatterns = [
    path('notes.html', views.notes, name='notes'),
]