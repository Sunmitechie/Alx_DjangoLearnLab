from django.urls import path
from .views import RegisterView, ProfileView, Login

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register'),
     path('profile/', ProfileView.as_view(), name='profile'),
     path('login/', Login.as_view(), name='login'),
]