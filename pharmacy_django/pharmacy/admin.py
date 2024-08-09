from django.contrib import admin
from .models import Ingredients, Categories, SideEffects, Allergies, Medicines

# Register your models here.
admin.site.register(Ingredients)
admin.site.register(Categories)
admin.site.register(SideEffects)
admin.site.register(Allergies)
admin.site.register(Medicines)
