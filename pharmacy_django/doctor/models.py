from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from administrator.models import Person


class SpecializationAvailable(models.Model):
    '''
        Stores all the specializations available
    '''
    
    specialization = models.CharField(max_length = 128, blank=False)

    def __str__(self):
        return f"{self.specialization}"

class Doctor(Person):
    '''
        Defines a user for the Doctor. Will contain additional information such as specialization, 
    '''

    # specialization = models.ForeignKey(SpecializationAvailable, blank=True, on_delete=models.PROTECT, related_name="doctors")
    consultation_fee = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    registration_number = models.CharField(blank=False, max_length=30)
    # availability = // To think of a way to represent availability
    is_verified = models.BooleanField(blank=False, default=False)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f"{self.first_name}{self.last_name}{self.registration_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} \n Registration Number: {self.registration_number} \n Consultation_fee: {self.consultation_fee}"


class Qualification(models.Model):
    '''
        Table to store qualifications of a doctor
    '''
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="qualifications")
    degree_name = models.TextField(blank=False)
    institution_name = models.TextField(blank=False)
    year_of_completion = models.IntegerField(blank=False)
    
    def __str__(self):
        return f"{self.doctor.name} - {self.degree_name} from {self.institution_name} on {self.year_of_completion}"


class Patient(Person):
    '''
        Inherits Person model and stores details for Patient, including medical history, primary physician
    '''
    medical_history = models.TextField(blank=True) # Placeholder field. To be made something more concrete.
    primary_physician = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True, blank=True, related_name="patients")

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
        To be made encrypted and can only be accessed by the doctor.
        # To make a lot more changes. To efficiently find a way to prescribe medicines.
        This table will be used to train the machine learning model.
    '''
    
    appointment = models.ForeignKey(Appointment, on_delete=models.PROTECT, related_name="prescription")
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name="prescriptions")