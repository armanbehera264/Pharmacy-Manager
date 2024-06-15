from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Doctor

# To update password and confirmPassword. Hash it. Don't serialize
class SigninSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True,
        required=True
    )
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'primary_phone_number', 'secondary_phone_number', 'email', 'password', 'age', 'gender', 'dob', 'address', 'consultation_fee', 'registration_number', 'experience']
    
    def validate_gender(self, value):
        valid_genders = ['Male', 'Female', 'Other']
        
        if value not in valid_genders:
            raise serializers.ValidationError("Invalid gender value. Must be one of: Male, Female, Other")
        return value
    
    def create(self, validated_data):
        '''
            Create and return a new Doctor instance
        '''
        # Fields to add in the frontend: specialization
        validated_data['password'] = make_password(validated_data.get('password'))
        return Doctor.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        '''
            Updates the instance
        '''
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.primary_phone_number = validated_data.get('primary_phone_number', instance.primary_phone_number)
        instance.secondary_phone_number = validated_data.get('secondary_phone_number', instance.secondary_phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.consultation_fee = validated_data.get('consultation_fee', instance.consultation_fee)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.registration_number = validated_data.get('registration_number', instance.registration_number)
        instance.is_verified = validated_data.get('is_verified', instance.is_verified)
        
        instance.save()
        return instance