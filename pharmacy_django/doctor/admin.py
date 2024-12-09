from django.contrib import admin
from .models import DoctorUser, PatientUser, SpecializationAvailable

admin.site.register(DoctorUser)
admin.site.register(PatientUser)
admin.site.register(SpecializationAvailable)