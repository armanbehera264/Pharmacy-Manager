from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(AbstractUser):
    
    '''
        Stores the details of an abstract person. Serves as a template for Patient, Doctor, Admin and other Employees.
        
        Implicit fields created: username, password, email, first_name, last_name, is_active, is_staff,
            is_superuser, last_login and date_joined
    '''
    
    age = models.IntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(150)])
    gender = models.CharField(blank=False, max_length=6)
    dob = models.DateField(auto_now=True, verbose_name="Date of Birth")
    address = models.TextField(blank=True)
    occupation = models.CharField(max_length=64, blank=True)
    primary_phone_number = models.CharField(max_length=15, blank=False)
    secondary_phone_number = models.CharField(max_length=15, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.first_name}{self.last_name}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Name: {self.username} \nAge: {self.age}"
