from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from administrator.models import User
class DoctorUser(models.Model):
    # specialization = models.ManyToManyField(SpecializationAvailable, blank=True, on_delete=models.PROTECT, related_name="doctors")
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.RESTRICT)
    consultation_fee = models.IntegerField(validators=[MinValueValidator(0)], blank=False, default=None)
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], blank=True, default=None)
    registration_number = models.CharField(unique=True, blank=False, default=None, max_length=50)
    # availability = // To think of a way to represent availability

    def __str__(self):
        # If the below line shows error on self.user.username, dont worry it works
        return f"Username: {self.user.username}\nRegistration Number: {self.registration_number}"

class PatientUser(models.Model):
    
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.PROTECT)
    medical_history = models.TextField(blank=True)