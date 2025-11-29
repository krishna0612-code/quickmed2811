from django.db import models
from users.models import CustomUser

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("upcoming", "Upcoming"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    patient = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="patient_appointments"
    )
    doctor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="doctor_appointments"
    )

    date = models.DateField()
    time = models.TimeField()
    age = models.IntegerField(null=True, blank=True)
    issue = models.TextField()
    duration = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    requested_date = models.DateField(null=True, blank=True)
    cancelled_date = models.DateField(null=True, blank=True)
    cancelled_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.fullName} - {self.status} - {self.date}"
