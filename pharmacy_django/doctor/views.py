from django.shortcuts import render
from rest_framework import views, response, status, permissions, exceptions
from administrator.models import User
from .models import DoctorUser
from .serializers import DoctorSerializer
from . import services

class SignIn(views.APIView):
    '''
        API view for doctor signin
    '''
    permission_classes = [permissions.AllowAny]  
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
            print(request.data)
            print(serializer.errors)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LogIn(views.APIView):
    '''
        APIView for doctor login
    '''
    permission_classes = [permissions.AllowAny]
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
        
        resp.set_cookie(key="jwt", value=token, httponly=True)
        
        return resp
        
        