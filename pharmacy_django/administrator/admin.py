from django.contrib import admin
from .models import User, SpecializationAvailable

# Register your models here.
admin.site.register(User)
admin.site.register(SpecializationAvailable)
