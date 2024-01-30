from django.db import models
from django.contrib.auth.models import User
from course.models import Course
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.user.username
    
class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,default=None, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.student.username