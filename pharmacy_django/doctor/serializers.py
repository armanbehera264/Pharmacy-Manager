from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import DoctorUser, PatientUser, SpecializationAvailable
from administrator.models import User
from administrator.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(many=False)
    class Meta:
        
        model = DoctorUser
        fields = ['user', 'consultation_fee', 'experience', 'registration_number']
        
    def create(self, validated_data):
        user_data = validated_data['user']
        # doctor_data = validated_data.pop('user')
        
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        # If the below line shows an error, it's not
        doctor = DoctorUser.objects.create(**validated_data)
        
        return doctor
        
        
class PatientSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(many=False) 
    
    class Meta:
        
        models = PatientUser
        fields = '__all__'
        
    def create(self, validated_data):
        user_data = validated_data['user']
        
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        # If the below line shows an error, it's not
        patient = PatientUser.objects.create(**validated_data)
        
        return patient

class SpecializationSerializer(serializers.ModelSerializer):
    '''
        Serializer for specialization serializer
    '''
    
    class Meta:
        model = SpecializationAvailable
        fields = '__all__'