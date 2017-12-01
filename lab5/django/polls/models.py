from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class films(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    objects = models.Manager()

    def __unicode__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=255)