from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('verifyEmployees/', views.VerifyEmployees.as_view(), name='verifyEmployees'),
    path('viewEmployees/', views.ViewEmployees.as_view(), name='viewEmployees'),
    path('viewMedicines/', views.ViewMedicines.as_view(), name='viewMedicines'),
    path('addMedicines/', views.AddMedicines.as_view(), name="addMedicines"),
]
