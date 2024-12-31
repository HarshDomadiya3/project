from django.contrib import admin
from myapp.models import students
from myapp.models import Doctor
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display=('fname','lname')

admin.site.register(students,studentadmin)

class doctoradmin(admin.ModelAdmin):
    list_display=('name','specialty','phone_number','email')

admin.site.register(Doctor,doctoradmin)
