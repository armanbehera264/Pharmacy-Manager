'''from django.contrib.auth import login, logout
from django.contrib.auth.models import AnonymousUser
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny, IsAuthenticated

# Importing tables from database
from .serializers import SigninSerializer
from .models import Doctor

class SignIn(APIView):
    ''
        API view for doctor signin
    ''
    permission_classes = [AllowAny]  
    def post(self, request, format=None):
        ''
        Only post methods are allowed for this endpoint.
        The data posted is stored in Doctor model.
        ''
        
        request.data['data']['dob'] = request.data['data']['dob'][:10]
        serializer = SigninSerializer(data=request.data['data'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(request.data)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LogIn(APIView):
    ''
    API view for doctor log in
    ''
    
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        ''
        Only post methods are allowed for this endpoint.
        The data posted is checked against Doctor model and is_verified is updated.
        ''
        print(request.data['data'])
        data = request.data.get("data", {})
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        registration = data.get("registration")
        password = data.get("password")
        username = f"{first_name}{last_name}{registration}"
        user = Doctor.objects.filter(username=username).first()
        
        # if user and user.check_password(password) and user.is_verified: // If condition after admin is implemented
        
        if user and user.check_password(password):
            login(request, user)
            request.session['username'] = username
            request.session['usertype'] = 'doctor'
            
            if request.user is not AnonymousUser:
                # User is logged in
                # You can access user data using request.user attributes
                print(f"Logged in user: {request.user.username}")
            else:
                # User is not logged in
                print("Anonymous user")
            
            return Response("Successfully logged in user.", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Incorrect username, password or unverified account.", status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    ''
    API view for doctor logout
    ''
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):

        print('\nEnteredasdas')
        if request.user.is_authenticated:
            print('\nEntered')
            print(f'\n\n{request.user}\n{request.user.is_authenticated}\n\n')
        
        if request.user is not AnonymousUser:
            logout(request)
            return Response("Successfully logged out user.", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Anonymous user. Cannot log out.", status=status.HTTP_406_NOT_ACCEPTABLE) '''