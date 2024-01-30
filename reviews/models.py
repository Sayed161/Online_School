from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/',default=None)
    Message = models.TextField()

    def __str__(self):
        return self.name