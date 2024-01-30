from rest_framework import serializers
from .models import Course,Category,Lesson
class Course_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Lesson_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'