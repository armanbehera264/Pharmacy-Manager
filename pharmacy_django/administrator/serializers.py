from rest_framework import serializers, exceptions

from .models import User, SpecializationAvailable

class UserSerializer(serializers.ModelSerializer):
    '''
        Serializer for base user model
    '''
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        '''
            Meta data for the base user model. Contains all fields and overrides the optional ones.
        '''
        model = User
        fields = '__all__' # Uses all the fields defined in the model User
        
    # Had to override the default implementation because functionality was conflicting with password check
    def create(self, validated_data):
        user_data = validated_data
        # doctor_data = validated_data.pop('user')
        
        user = User.objects.create_user(**user_data)
        
        return user
    
    def validate(self, attrs):
        
        if attrs['role'] in ['Admin', 'Doctor', 'Employee']:
            try:
                email = attrs['email']
                password = attrs['password']
            except KeyError:
                raise exceptions.ValidationError(detail="Email or Password not provided for non-Patient roles.")
            
        return attrs
            
    def validate_role(self, value):
        if value not in ['Admin', 'Doctor', 'Employee', 'Patient']:
            raise exceptions.ValidationError(detail="Role of the user can only have four values: 'Admin', 'Doctor', 'Employee' and 'Patient'")
        return value
        
    def validate_gender(self, value):
        if value not in ['Male', 'Female', 'Other']:
            raise exceptions.ValidationError(detail="Gender of the user can only have three values: 'Male', 'Female' or 'Other'")
        return value
    
class SpecializationSerializer(serializers.ModelSerializer):
    '''
        Serializer for specialization serializer
    '''
    
    class Meta:
        model = SpecializationAvailable
        fields = '__all__'