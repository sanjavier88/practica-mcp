from django.db import models

class Appointment(models.Model):
    TREATMENT_CHOICES = [
        ('Consulta General', 'Consulta General'),
        ('Blanqueamiento Dental', 'Blanqueamiento Dental'),
        ('Odontología Cosmética', 'Odontología Cosmética'),
        ('Implantología', 'Implantología'),
        ('Urgencia', 'Urgencia'),
    ]

    SPECIALIST_CHOICES = [
        ('Odontología General', 'Odontología General'),
        ('Odontopediatría', 'Odontopediatría'),
        ('Ortodoncista', 'Ortodoncista'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    treatment = models.CharField(max_length=100, choices=TREATMENT_CHOICES)
    specialist = models.CharField(max_length=100, choices=SPECIALIST_CHOICES)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita de {self.name} para {self.treatment}"