from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def atencion(request):
    return render(request, 'website/atencion.html')

def especialidades(request):
    return render(request, 'website/especialidades.html')

def services(request):
    return render(request, 'website/services.html')