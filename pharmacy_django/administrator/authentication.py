from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from .models import User

class CustomUserAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
        # tries to get the 'jwt' cookie from database
        token = request.COOKIES.get("jwt")
        
        # if the token does not exist
        if not token:
            return None
        
        # Tries to decode the token
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms="HS256")
        except jwt.exceptions.DecodeError as e:
            raise exceptions.AuthenticationFailed(f"Unauthorized {e}")
        
        # Returns a user that is decoded from the token
        user = User.objects.filter(id=payload["id"]).first()
        
        return (user, None)
    

class CustomDoctorAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        
         # tries to get the 'jwt' cookie from database
        token = request.COOKIES.get("jwt")
        
        # if the token does not exist
        if not token:
            return None
        
        # Tries to decode the token
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")
        
        # Returns a user that is decoded from the token
        user = User.objects.filter(id=payload["id"]).first()
        
        if user.role != 'Doctor':
            raise exceptions.AuthenticationFailed("Unauthorized. Only users with doctor role are allowed in this point.")
        
        return (user, None)