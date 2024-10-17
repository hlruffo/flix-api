from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie


# Create your views here.
class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer