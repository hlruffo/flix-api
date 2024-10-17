from django.shortcuts import render
from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer


# Create your views here.
class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer