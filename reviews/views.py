from django.shortcuts import render
from rest_framework import viewsets
from .models import Review
from .serializers import review_Serializer
# Create your views here.
class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = review_Serializer
