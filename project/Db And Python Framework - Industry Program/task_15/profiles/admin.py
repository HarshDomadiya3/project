from django.contrib import admin

# Register your models here.
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'gender', 'availability', 'phone', 'email')
    list_filter = ('specialty', 'availability', 'gender')
    search_fields = ('name', 'specialty', 'phone')
    ordering = ('name',)
    
    # Adding a detailed view in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'gender', 'specialty', 'availability')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email')
        }),
    )

admin.site.register(Doctor, DoctorAdmin)
