from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact_details']
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'contact_details']

    def validate_specialty(self, value):
        allowed_specialties = ['Cardiology', 'Dermatology', 'Pediatrics']
        if value not in allowed_specialties:
            raise serializers.ValidationError(f"Specialty must be one of {allowed_specialties}.")
        return value
