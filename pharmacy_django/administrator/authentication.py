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


class CustomAdminAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request)
        
        print("aksfbhkajs")

        if response is not None:
            # unpacking
            user, token = response
            print("adjasjf")
            print(f"Authenticated User: {user}, Token: {token}")
            print()
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.')
        
        if user.role != 'Admin':
            raise exceptions.PermissionDenied("Unauthorized.")
        
        if user.is_superuser == False:
            raise exceptions.PermissionDenied('Unauthorized.')
        
        return (user, None)


class CustomDoctorAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request) # This returns None if the request was unable to be authenticated
        
        if response is not None:
            # unpacking
            user, token = response
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.') # Raises a 401 error
        
        if user.role != 'Doctor':
            raise exceptions.PermissionDenied("Unauthorized.") # Raises a 403 error
        
        return (user, None)
    

class CustomPharmacyAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request)
        
        if response is not None:
            # unpacking
            user, token = response
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.')
        
        if user.role != 'Pharmacy':
            raise exceptions.PermissionDenied("Unauthorized.")
        
        return (user, None)
    
    
class CustomFrontDeskAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        JWT_authenticator = JWTAuthentication()
        
        # Checks the request for validity
        response = JWT_authenticator.authenticate(request)
        
        if response is not None:
            # unpacking
            user, token = response
        else:
            raise exceptions.AuthenticationFailed('Invalid Access Token.')
        
        if user.role != 'FrontDesk':
            raise exceptions.PermissionDenied("Unauthorized.")
        
        return (user, None)