from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer   

def home(request):
    return render(request, 'home.html')

    
