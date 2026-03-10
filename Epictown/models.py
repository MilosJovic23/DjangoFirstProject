from django.db import models

class Comicbook(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    format = models.CharField(max_length=25)
    ImgUrl = models.ImageField(upload_to='images')
    author = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return self.title
