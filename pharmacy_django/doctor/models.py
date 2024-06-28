from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from administrator.models import Person
from django.contrib.auth.models import BaseUserManager

from administrator.models import SpecializationAvailable

class DoctorManager(BaseUserManager):
    
    def create_user(self, first_name: str, last_name: str, email: str, password: str, age: int, gender: str, dob: models.DateField, primary_phone_number: str, secondary_phone_number: str, consultation_fee: int, experience: int, registration_number: str, is_verified: bool, is_superuser: bool) -> "User":
        if not first_name or not last_name or not email or not age or not gender or not primary_phone_number or not consultation_fee or not registration_number:
            raise ValueError("User must provide proper credentials for creating user.")
        
        user = self.model(
            registration_number=registration_number,
            email=self.normalize_email(email),
            secondary_phone_number = secondary_phone_number
        )
        user.first_name = first_name
        user.last_name = last_name
        user.age = age
        user.gender = gender
        user.dob = dob
        user.primary_phone_number = primary_phone_number
        user.secondary_phone_number = secondary_phone_number
        user.consultation_fee = consultation_fee
        user.experience = experience
        user.registration_number = registration_number
        user.is_verified = False
        user.is_staff = True
        user.is_active = True
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, first_name: str, last_name: str, email: str, password: str, age: int, gender: str, dob: models.DateField, primary_phone_number: str, secondary_phone_number: str, consultation_fee: int, experience: int, registration_number: str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            age=age,
            gender=gender,
            dob=dob,
            primary_phone_number=primary_phone_number,
            secondary_phone_number=secondary_phone_number,
            consultation_fee=consultation_fee,
            experience=experience,
            registration_number=registration_number,
            is_verified=True,
            is_superuser=True
        )
        user.save()
                
class Doctor(Person):
    '''
        Defines a user for the Doctor. Will contain additional information such as specialization, 
    '''

    # specialization = models.ForeignKey(SpecializationAvailable, blank=True, on_delete=models.PROTECT, related_name="doctors")
    consultation_fee = models.IntegerField(validators=[MinValueValidator(0)])
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
    registration_number = models.TextField(unique=True)
    # availability = // To think of a way to represent availability
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'registration_number'
    REQUIRED_FIELDS = ['consultation_fee', 'age', 'gender', 'primary_phone_number']
    
    objects = DoctorManager()

    def __str__(self):
        return f"Registration Number: {self.registration_number} \n Consultation_fee: {self.consultation_fee}"


class Patient(Person):
    '''
        Inherits Person model and stores details for Patient, including medical history, primary physician
    '''
    medical_history = models.TextField(blank=True) # Placeholder field. To be made something more concrete.
    occupation = models.TextField(blank=True)    

    # As patient does not require a password to be registered, the next two methods override the default methods so that no password is set
    def set_password(self, raw_password):
        pass

    def check_password(self, raw_password):
        return True

    def __str__(self):
        return f"Patient: {self.username}"

    
class Appointment(models.Model):
    '''
        Stores the appointment detail of the patient with the doctor
    '''
    doctorRequired = models.ForeignKey(SpecializationAvailable, on_delete=models.PROTECT, related_name="appointment")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointment")
    date = models.DateField()
    time = models.TimeField()
    concern = models.TextField()
   
    
class Prescription(models.Model):
    '''
        Stores the appointment as well as the prescription details of the Patient.
        To be made encrypted and can only be accessed by the doctor using permissions.
        # To make a lot more changes. To efficiently find a way to prescribe medicines.
        This table will be used to train the machine learning model.
    '''
    
    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT, related_name="prescription")
    doctor = models.ManyToManyField(Doctor, related_name="prescriptions")