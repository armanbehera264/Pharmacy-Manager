from django.contrib import admin
from .models import Doctor, SpecializationAvailable, Qualification

# Register your models here.
admin.site.register(Doctor)
admin.site.register(SpecializationAvailable)
admin.site.register(Qualification)