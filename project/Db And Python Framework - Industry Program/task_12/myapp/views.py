
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'myapp/doctor_list.html', {'doctors': doctors})


def doctor_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialization']
        phone = request.POST['phone']
        email = request.POST['email']
        Doctor.objects.create(name=name, specialization=specialization, phone=phone, email=email)
        return redirect('doctor_list')
    return render(request, 'myapp/doctor_form.html')


def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialization = request.POST['specialization']
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'myapp/doctor_form.html', {'doctor': doctor})


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'myapp/doctor_confirm_delete.html', {'doctor': doctor})
