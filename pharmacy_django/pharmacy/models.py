from django.db import models
from django.core.validators import MinValueValidator


class Ingredients(models.Model):
    '''
        Stores the ingredients information
    '''
    name = models.CharField(max_length=255, verbose_name="Ingredient Name", help_text="Name of the ingredient")

    def __str__(self):
        return self.name


class Categories(models.Model):
    '''
        Stores categories for medicines
    '''
    name = models.CharField(max_length=255, verbose_name="Category Name", help_text="Name of the category", blank=False)
    usage_priority = models.IntegerField(verbose_name="Usage Priority", help_text="Priority of this category for the medicine", blank=False)

    def __str__(self):
        return f"{self.name} (Priority: {self.usage_priority})"


class SideEffects(models.Model):
    '''
        Stores side effects of medicines
    '''
    name = models.CharField(max_length=255, verbose_name="Side Effect", help_text="Description of the side effect", blank=False)

    def __str__(self):
        return self.name


class Allergies(models.Model):
    '''
        Stores the allergies of the medicine
    '''
    name = models.CharField(max_length=255, verbose_name="Allergies", help_text="Allergy for the medicines", blank=False)
    
    def __str__(self):
        return self.name


class Medicines(models.Model):
    '''
        Stores the medicines value
    '''
    name = models.CharField(max_length=255, verbose_name="Medicine Name", help_text="Name of the medicine", blank=False)
    stock = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Stock", help_text="Stock quantity of the medicine", blank=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)], verbose_name="Price", help_text="Price of the medicine", blank=False)
    ingredients = models.ManyToManyField(Ingredients, verbose_name="Ingredients", help_text="Ingredients in the medicine")
    description = models.TextField(verbose_name="Description", blank=True, null=True, help_text="Description of the medicine")
    manufacturer = models.CharField(max_length=255, verbose_name="Manufacturer", help_text="Manufacturer of the medicine", blank=True)
    expiration_date = models.DateField(verbose_name="Expiration Date", blank=False, help_text="Expiration date of the medicine")
    categories = models.ManyToManyField(Categories, verbose_name="Categories", help_text="Categories of the medicine")
    sideEffects = models.ManyToManyField(SideEffects, verbose_name="Side Effects", help_text="Possible side effects of the medicine")
    allergies = models.ManyToManyField(Allergies, verbose_name="Allergies", help_text="Patients with these allergies should avoid.")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Medicines"
