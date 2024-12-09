from django.shortcuts import render
from rest_framework import views, response, status, permissions, exceptions
from administrator.models import User
from administrator.serializers import UserSerializer
from administrator import authentication
from doctor.serializers import DoctorSerializer
from pharmacy.models import Medicines, Allergies, SideEffects, Ingredients, Categories
from pharmacy.serializers import MedicinesSerializer, AllergiesSerializer, CategoriesSerializer, IngredientsSerializer, SideEffectsSerializer

class SignIn(views.APIView):
    '''
        API view for administrator signin
    '''
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        '''
        Only post methods are allowed for this endpoint.
        The data posted is stored in User model.
        '''
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            if user.is_verified == False or user.is_superuser == False:
                return exceptions.AuthenticationFailed("Sign In user details must be of a admin.")
            
            user = serializer.save()

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class VerifyEmployees(views.APIView):
    
    authentication_classes = (authentication.CustomAdminAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        
        unverifiedEmployees = User.objects.filter(is_verified=False)
        
        resp = []
            
        for user in unverifiedEmployees:
            user_serializer = UserSerializer(user)
            resp.append(user_serializer.data)
            
        return response.Response(resp)
    
    def post(self, request):
        
        # Credentials of the user to be set to verified
        ids = request.data['ids']
        code = request.data['code']
        
        try:
            for id in ids:
                user = User.objects.get(id=id)
                if code == 0:
                    user.is_verified = True
                    user.save()
                elif code == 1:
                    user.delete()
        except:
            return exceptions.NotAcceptable('Failed to delete users.')
        
        if code == 0:
            return response.Response('Users successfully verified.')
        elif code == 1:
            return response.Response('Users succesfully deleted.')
        else:
            return exceptions.NotAcceptable('The code provided is not a valid code.')
        

class ViewEmployees(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        
        users = User.objects.exclude(is_superuser=True)
        
        resp = []
        
        for user in users:
            user_serializer = UserSerializer(user)
            resp.append(user_serializer.data)
            
        return response.Response(resp)
    
    def post(self, request):
        
        ids = request.data['ids']
        
        try:
            for id in ids:
                user = User.objects.get(id=id)
                user.delete()
        except:
            return exceptions.NotAcceptable('Failed to delete users.')
            
        return response.Response('Users successfully deleted from system.')


class ViewMedicines(views.APIView):
    '''
        When it's a get request, this API returns all the medicines available
        When it's a post request, this API allows to edit the medicine
    '''
    
    authentication_classes = (authentication.CustomDoctorAuthentication, authentication.CustomAdminAuthentication, authentication.CustomPharmacyAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        
        medicines = Medicines.objects.all()
        
        resp = []
        
        for medicine in medicines:
            medicine_serialized = MedicinesSerializer(medicine)
            resp.append(medicine_serialized.data)
        
        return response.Response(resp)
    
    def post(self, request):
        
        try:
            id = request.data['id']
            
            medicine = Medicines.objects.get(id=id)
            
            medicine.name = request.data.get('name', medicine.name)
            medicine.stock = request.data.get('stock', medicine.stock)
            medicine.expiration_date = request.data.get('expiration_date', medicine.expiration_date)
            medicine.price = request.data.get('price', medicine.price)
            medicine.manufacturer = request.data.get('manufacturer', medicine.manufacturer)
            medicine.description = request.data.get('description', medicine.description)
            
            medicine.save()
            
            return response.Response({"message": "Medicine updated successfully."}, status=status.HTTP_200_OK)
            
        except Medicines.DoesNotExist:
            return response.Response({"error": "Medicine not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return response.Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    

class AddMedicines(views.APIView):
    '''
        Add Medicines endpoint
    '''
    
    authentication_classes = (authentication.CustomAdminAuthentication, authentication.CustomPharmacyAuthentication)
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request):
        allergies = Allergies.objects.all()
        ingredients = Ingredients.objects.all()
        sideEffects = SideEffects.objects.all()
        categories = Categories.objects.all()
        
        resp = {
            'allergies': [],
            'ingredients': [],
            'sideEffects': [],
            'categories': []
        }
        
        for allergy in allergies:
            serialized = AllergiesSerializer(allergy)
            resp['allergies'].append(serialized.data)  # Use .data to get JSON serializable data
            
        for ingredient in ingredients:
            serialized = IngredientsSerializer(ingredient)
            resp['ingredients'].append(serialized.data)  # Use .data to get JSON serializable data
            
        for sideEffect in sideEffects:
            serialized = SideEffectsSerializer(sideEffect)  # Add 'Serializer' to the class name
            resp['sideEffects'].append(serialized.data)  # Use .data to get JSON serializable data
            
        for category in categories:
            serialized = CategoriesSerializer(category)
            resp['categories'].append(serialized.data)  # Use .data to get JSON serializable data
            
        return response.Response(resp)


    def post(self, request):
        
        ingredients_data = request.data.pop('ingredients', [])
        categories_data = request.data.pop('categories', [])
        sideEffects_data = request.data.pop('sideEffects', [])
        allergies_data = request.data.pop('allergies', [])

        # Create the Medicines object
        serializer = MedicinesSerializer(data=request.data)
        
        if not ingredients_data or not categories_data or not sideEffects_data or not allergies_data:
            return response.Response("All required fields are not provided.", status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            medicine = serializer.save()

            for ingredient_data in ingredients_data:
                ingredient, created = Ingredients.objects.get_or_create(**ingredient_data)
                medicine.ingredients.add(ingredient)
            
            for category_data in categories_data:
                category, created = Categories.objects.get_or_create(**category_data)
                medicine.categories.add(category)
            
            for sideEffect_data in sideEffects_data:
                side_effect, created = SideEffects.objects.get_or_create(**sideEffect_data)
                medicine.sideEffects.add(side_effect)
                
            for allergy_data in allergies_data:
                allergy, created = Allergies.objects.get_or_create(**allergy_data)
                medicine.allergies.add(allergy)

            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(views.APIView):
    '''
        Logout view can only be accessed by authenticated users
    '''
    authentication_classes = (authentication.CustomAdminAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )
    
    def post(self, request):
        resp = response.Response()
        # resp.delete_cookie("jwt")
        
        resp.data = {"message": "Successfully logged out user."}
        
        return resp