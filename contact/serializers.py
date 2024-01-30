from rest_framework import serializers
from .models import Contact
class contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'