from django.db import models
import json

class Shape(models.Model):
    name = models.CharField(max_length=100)
    attributes = models.CharField(max_length=200)

    def Name(self):
        return self.name

    @property
    def Attributes(self):
        attrDict = json.loads(self.attributes)
        params = []
        for name, val in attrDict.items():
            str1 = name + "=" + val
            params.append(str1)
        print(" ".join(params))
        return " ".join(params)

    def __str__(self):
        return self.name

class Scene(models.Model):
    shapes = models.ManyToManyField(Shape)

class Projection(models.Model):
    proj1 = models.CharField(max_length=50)



# Create your models here.
