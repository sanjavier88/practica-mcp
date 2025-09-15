from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('atencion/', views.atencion, name='atencion'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('services/', views.services, name='services'),
]
