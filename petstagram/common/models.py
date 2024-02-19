from django.db import models
from petstagram.pets.models import Pet


# Create your models here.

class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()
