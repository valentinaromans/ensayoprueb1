from django.urls import path
from . import views

urlpatterns = [
    path('', views.jony, name='jony'),
    path('vale/', views.vale, name='vale')
]