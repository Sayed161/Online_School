from django.shortcuts import render
from rest_framework import viewsets
from .filters import LessonFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course,Category,Lesson
from .serializers import category_Serializer, Course_Serializer,Lesson_Serializer
# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = Course_Serializer

class LessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = Lesson_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LessonFilter
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = category_Serializer