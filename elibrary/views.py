from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BookSerializer

# Create your views here.

# we perform crud operations here and the way we want to view our data here
class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer   