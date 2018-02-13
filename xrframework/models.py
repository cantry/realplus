from django.db import models
from django.core import serializers

class Shapes(models.Model):
    name = models.CharField(max_length=100)
    attributes = models.CharField(max_length=200)

    def Name(self):
        return self.name

    def Attributes(self):
        return self.attributes

    def AttributesJSON(self):
        return serializers.serialize("json", attributes)

    def __str__(self):
        return self.name



class Scene(models.Model):
    shapes = models.CharField(max_length = 100)




# Create your models here.
