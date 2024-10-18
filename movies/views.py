from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Movie


# Create your views here.
class MovieListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer