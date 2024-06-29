from django.shortcuts import render
from rest_framework import views, response, status, permissions

# Create your views here.
from .serializers import UserSerializer
class SignIn(views.APIView):
    '''
        API view for doctor signin
    '''
    permission_classes = [permissions.AllowAny]  
    def post(self, request, format=None):
        '''
        Only post methods are allowed for this endpoint.
        The data posted is stored in Doctor model.
        '''
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(request.data)
            print(serializer.errors)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        