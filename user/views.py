from django.shortcuts import render, redirect, get_object_or_404
from user.models import Appointment

def formulario_cita(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        treatment = request.POST.get('services')
        specialist = request.POST.get('department')
        message = request.POST.get('messages')

        appointment = Appointment.objects.create(
            name=name,
            email=email,
            treatment=treatment,
            specialist=specialist,
            message=message
        )
        return redirect('appointment_detail', pk=appointment.pk) # Redirect to the detail page

    return render(request, 'website/formulario-cita.html')

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'user/appointment_detail.html', {'appointment': appointment})