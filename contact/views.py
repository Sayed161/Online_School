from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import contact_Serializer
# Create your views here.
class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = contact_Serializer