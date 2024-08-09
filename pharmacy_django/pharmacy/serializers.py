from rest_framework import serializers, exceptions
from .models import Ingredients, Categories, SideEffects, Allergies, Medicines

class IngredientsSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Ingredients
        fields = '__all__'
        
    def create(self, validated_data):
        
        object = Ingredients.objects.create(**validated_data)
        
        return object
    

class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Categories
        fields = '__all__'
        
    def create(self, validated_data):
        
        object = Categories.objects.create(**validated_data)

        return object
    
    
class SideEffectsSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = SideEffects
        fields = '__all__'
        
    def create(self, validated_data):
        
        object = SideEffects.objects.create(**validated_data)
        
        return object
    

class AllergiesSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Allergies
        fields = '__all__'
        
    def create(self, validated_data):
        
        object = Allergies.objects.create(**validated_data)
        
        return object
    

class MedicinesSerializer(serializers.ModelSerializer):
    
    # Check how ingredients are saved when multiple ingredients are saved and also how many=True works
    ingredients = IngredientsSerializer(many=True, required = False)
    allergies = AllergiesSerializer(many=True, required = False)
    sideEffects = SideEffectsSerializer(many=True, required = False)
    categories = CategoriesSerializer(many=True, required = False)
    
    class Meta:
        
        model = Medicines
        fields = '__all__'
        
    def create(self, validated_data):
        medicine = Medicines.objects.create(**validated_data)

        return medicine
        