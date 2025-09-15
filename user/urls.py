from django.urls import path
from . import views

urlpatterns = [
    path('formulario-cita/', views.formulario_cita, name='formulario-cita'),
    path('<int:pk>/detail/', views.appointment_detail, name='appointment_detail'),
]