from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Userus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    nickname = models.CharField(max_length=30, null=True)


class Film(models.Model):
    # added_by = models.ForeignKey(Userus, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=255,null=True)
    img = models.FileField(upload_to='images', default='images/def.jpg')

    # objects = models.Manager()

class Review(models.Model):
    user = models.ForeignKey(Userus, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_date = models.DateField()
    review_content = models.CharField(max_length=255, null=True)