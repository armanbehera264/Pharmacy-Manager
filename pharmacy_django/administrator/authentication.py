from django.conf import settings
from rest_framework import authentication, exceptions
import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User

class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request)
        
        if response is not None:
            # unpacking
            user, token = response
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.')
        
        return (user, None)
    

class CustomDoctorAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request)
        
        if response is not None:
            # unpacking
            user, token = response
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.')
        
        if user.role != 'Doctor':
            raise exceptions.PermissionDenied("Unauthorized.")
        
        return (user, None)