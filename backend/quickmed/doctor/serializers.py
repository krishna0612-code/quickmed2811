from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patientName = serializers.CharField(source="patient.fullName", read_only=True)
    patientId = serializers.IntegerField(source="patient.id", read_only=True)
    doctorName = serializers.CharField(source="doctor.fullName", read_only=True)
    doctorId = serializers.IntegerField(source="doctor.id", read_only=True)

    class Meta:
        model = Appointment
        fields = "__all__"
