from django.shortcuts import render
from rest_framework import views, response, status, permissions, exceptions
from administrator.models import User
from administrator.serializers import UserSerializer
from administrator import services, authentication
from doctor.serializers import DoctorSerializer

class SignIn(views.APIView):
    '''
        API view for doctor signin
    '''
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        '''
        Only post methods are allowed for this endpoint.
        The data posted is stored in User model.
        '''
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            if user.is_verified == False or user.is_superuser == False:
                user.delete()
                return exceptions.AuthenticationFailed("Sign In user details must be of a admin.")
            
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
        
        if user.is_verified == False or user.is_superuser == False:
                return exceptions.AuthenticationFailed("Sign In user details must be of a admin.")
        
        token = services.create_token(user_id=user.id)
        
        resp = response.Response()
        
        # resp.set_cookie(key="jwt", value=token, httponly=True)
        
        resp.data = {"jwt": token}
        
        return resp
        

class VerifyEmployees(views.APIView):
    
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        
        unverifiedDoctors = User.objects.filter(role='Doctor', is_verified=False)
        unverifiedEmployees = User.objects.filter(role='Employee', is_verified=False)
        
        resp = []
        
        for user in unverifiedDoctors:
            user_serializer = UserSerializer(user)
            resp.append(user_serializer.data)
            
        for user in unverifiedEmployees:
            user_serializer = UserSerializer(user)
            resp.append(user_serializer.data)
            
        return response.Response(resp)
    
    def post(self, request):
        
        # Credentials of the user to be set to verified
        username = request.data['username']
        
        user = User.objects.get(username=username)
        user.is_verified = True
        
        return response.Response('User successfully verified.')

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
        