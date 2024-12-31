from django.shortcuts import render,get_object_or_404, redirect
from .models import Doctor


# Create your views here.

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialty = request.POST.get('specialty')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        Doctor.objects.create(name=name, specialty=specialty, email=email, phone_number=phone_number)
        return redirect('doctor_list')
    return render(request, 'doctors/add_doctor.html')

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialty = request.POST.get('specialty')
        doctor.email = request.POST.get('email')
        doctor.phone_number = request.POST.get('phone_number')
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctors/edit_doctor.html', {'doctor': doctor})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})