from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Ingredients(models.Model):
    '''
        Stores the ingredients that make up a medicine.
        Will be auto-updated if the ingredient already doesn't exist
    '''
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank = True)
    
    def __str__(self):
        return f"{self.name}"


class Medicine(models.Model):
    '''
        Stores the medicines, their constituent ingredients, dosage, age group for that dosage
        A new field can be created for the same medicine if the age is different for different dosage
        If it is identified that different age groups can have same dosage dosgae value will be updated
        Dosage will be in the format "x medicines for y times of day (before or after)"
        ML model will be used to fill up the blank data fields
    '''
    name = models.CharField(max_length=128, blank=False)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.PROTECT, related_name="medicines")
    description = models.TextField(blank=True)
    quantityAvailable = models.IntegerField(blank=True, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.name}: {self.description}"