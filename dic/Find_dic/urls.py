from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.process_data),
    path('submit', views.process_data)
]
