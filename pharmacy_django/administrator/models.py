from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(AbstractUser):
    
    '''
        Stores the details of an abstract person. Serves as a template for Patient, Doctor, Admin and other Employees.
        
        Implicit fields created: username, password, email, first_name, last_name, is_active, is_staff,
            is_superuser, last_login and date_joined
    '''
    
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    
    genderChoices = {
        'M': 'Male',
        'F': 'Female',
        'O': 'Other'
    }
    gender = models.CharField(choices=genderChoices)
    
    
    dob = models.DateField(auto_now=True, verbose_name="Date of Birth")
    primary_phone_number = models.CharField(max_length=15)
    secondary_phone_number = models.CharField(max_length=15)
    
    roleChoices = {
        'Admin': 'Admin',
        'Doctor': 'Doctor',
        'Employee': 'Employee',
        'Patient': 'Patient'
    } 
    role = models.CharField(choices=roleChoices)
    
    REQUIRED_FIELDS = ['age', 'gender', 'primary_phone_number']
    
    def __str__(self):
        return f"Name: {self.username} \nAge: {self.age}"
    

class SpecializationAvailable(models.Model):
    '''
        Stores all the specializations available
    '''
    
    specialization = models.CharField(max_length = 128, blank=False)

    def __str__(self):
        return f"{self.specialization}"

