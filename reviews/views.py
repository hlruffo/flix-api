from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ReviewListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
