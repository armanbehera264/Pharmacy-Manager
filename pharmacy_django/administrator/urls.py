from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]
