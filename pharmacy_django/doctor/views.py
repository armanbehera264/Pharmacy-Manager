from django.shortcuts import render
from rest_framework import views, response, status, permissions, exceptions
from administrator.models import User
from .models import DoctorUser
from .serializers import DoctorSerializer
from administrator.serializers import UserSerializer
from administrator import services, authentication
import jwt
from django.conf import settings

class SignIn(views.APIView):
    '''
        API view for doctor signin
    '''
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        '''
        Only post methods are allowed for this endpoint.
        The data posted is stored in Doctor model.
        '''
        
        serializer = DoctorSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LogIn(views.APIView):
    '''
        APIView for doctor login
    '''
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        '''
            Only post methods are allowed for this endpoint.
            The data posted is used to login the user
        '''
        
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid password.')
        
        token = services.create_token(user_id=user.id)
        
        resp = response.Response()
        
        # resp.set_cookie(key="jwt", value=token, httponly=True)
        
        resp.data = {"jwt": token}
        
        return resp
        

class res(views.APIView):
    permission_classes  =(permissions.AllowAny, )
    
    def post(self, request):
        
        '''
            eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNzIxMTkzMTYwLCJpYXQiOjE3MjExMDY3MDB9.nqdfgWcXDugRfXYRX51NJ4hraGmFNL5VoB7GbaDbTvQ
        '''
        
        cookie = request.data['cookie']
        
        try:
            payload = jwt.decode(cookie, settings.JWT_SECRET, algorithms=["HS256"])
        except jwt.exceptions.DecodeError as e:
            raise exceptions.AuthenticationFailed(f"Unauthorized {e}")
        
        # Returns a user that is decoded from the token
        user = User.objects.filter(id=payload["id"]).first()  
        
        serializer = UserSerializer(user)
        
        return response.Response(serializer.data)

class DoctorAPI(views.APIView):
    '''
        This viewpoint can only be used if the user is authenticated.
        This API does not do anything, just an example of how a view can be set which is only accessible to user who are authenticated.
    '''
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        user = request.user
        
        serializer = UserSerializer(user)
        
        return response.Response(serializer.data)
        

class PatientAPI(views.APIView):
    '''
        This viewpoint can only be used if the user is authenticated and the user is a doctor.
        This API also does not do anything, just an example for an API with doctor and authenticated requirements.
    '''
    authentication_classes = (authentication.CustomDoctorAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        pass
    

class Logout(views.APIView):
    '''
        Logout view can only be accessed by authenticated users
    '''
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self, request):
        resp = response.Response()
        # resp.delete_cookie("jwt")
        
        resp.data = {"message": "Successfully logged out user."}
        
        return resp
        