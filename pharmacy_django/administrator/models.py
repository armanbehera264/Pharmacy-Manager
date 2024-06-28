from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    
    def create_user(self, username: str, age: int, gender: str, primary_phone_number: str,  role: str, is_verified: bool, occupation: str, is_staff: bool, is_active: bool, is_superuser: bool, email: models.EmailField, password: str, first_name: str, last_name: str, secondary_phone_number: str = ''):
        
        if not username:
            raise ValueError("Username of the user must be provided.")
        if not age:
            raise ValueError("Age of the user must be provided.")
        if not gender:
            raise ValueError("Gender of the user must be provided.")
        if not primary_phone_number:
            raise ValueError("Primary Phone Number of the user must be provided.")
        if not role:
            raise ValueError("Role of the user must be provided.")
        if not is_verified:
            raise ValueError("It must be provided if the user is verified or not.")
        if not occupation:
            raise ValueError("Occupation of the user must be provided.")
        
        if gender not in ['Male', 'Female', 'Other']:
            raise ValueError('The valid values for gender can only be \'Male\', \'Female\' or \'Other\'')
        
        if role not in ['Admin', 'Doctor', 'Employee', 'Patient']:
            raise ValueError('The valid values for role can only be \'Admin\', \'Doctor\', \'Employee\' or \'Patient\'')
        
        user = self.model(
            username = username,
            age = age,
            gender = gender,
            primary_phone_number = primary_phone_number,
            role = role,
            is_verified = is_verified,
            occupation = occupation,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        user.secondary_phone_number = secondary_phone_number
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save()
class User(AbstractUser):
    
    '''
        Stores the details of the base user model used ofr authentication. Serves as a template for Patient, Doctor and Employees.
        
        Implicit fields created from AbstractUser: username, password, email, first_name, last_name, is_active, is_staff,
            is_superuser, last_login and date_joined
    '''
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    
    genderChoices = {
        'M': 'Male',
        'F': 'Female',
        'O': 'Other'
    }
    gender = models.CharField(choices=genderChoices, max_length=6)
    
    primary_phone_number = models.CharField(max_length=15)
    secondary_phone_number = models.CharField(max_length=15)
    
    roleChoices = {
        'Admin': 'Admin',
        'Doctor': 'Doctor',
        'Employee': 'Employee',
        'Patient': 'Patient'
    } 
    role = models.CharField(choices=roleChoices, max_length=8)
    
    is_verified = models.BooleanField(default=False)
    occupation = models.CharField(max_length=50)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['age', 'gender', 'primary_phone_number', 'role', 'is_verified', 'occupation', 'email', 'password', 'first_name', 'last_name']
    
    def __str__(self):
        return f"Name: {self.username}"
    


class SpecializationAvailable(models.Model):
    '''
        Stores all the specializations available
    '''
    
    specialization = models.CharField(max_length = 128, blank=False)

    def __str__(self):
        return f"{self.specialization}"
    

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
