from django.http import JsonResponse
from django.shortcuts import render
from .models import DoctorProfile
from .forms import DoctorProfileForm

def add_doctor_profile(request):
    if request.method == 'POST' and request.is_ajax():
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Doctor added successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors})

def edit_doctor_profile(request, pk):
    if request.method == 'POST' and request.is_ajax():
        doctor = DoctorProfile.objects.get(pk=pk)
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Doctor updated successfully.'})
        else:
            return JsonResponse({'status': 'error', 'message': form.errors})


def delete_doctor_profile(request, pk):
    if request.method == 'POST' and request.is_ajax():
        doctor = DoctorProfile.objects.get(pk=pk)
        doctor.delete()
        return JsonResponse({'status': 'success', 'message': 'Doctor deleted successfully.'})

def doctor_profiles(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'profiles/doctor_profiles.html', {'doctors': doctors})
