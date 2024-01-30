from django.db import models
# Create your models here.
star = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    fee = models.CharField(max_length=30)
    ratings = models.CharField(choices=star, max_length=20,default=None)
    duration = models.CharField(max_length=12)
    lectures = models.IntegerField()
    instructor = models.CharField(max_length=120)
    category = models.ManyToManyField(Category)
    purchased = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="media/videos")
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    duration = models.CharField(max_length=20,default=None)