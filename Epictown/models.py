from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Comicbook(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    format = models.CharField(max_length=25)
    ImgUrl = models.ImageField(upload_to='images')
    author = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ])

    def __str__(self):
        return self.title
