from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student,Enrollment

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class enroll_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class Registration_Serializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password','confirm_password']

    def save(self, *args, **kwargs):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({'Error': "Password Doesn't Match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error': "Email Already Exists"})
        
        
        account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password)
        account.save()

class UserLogin(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
