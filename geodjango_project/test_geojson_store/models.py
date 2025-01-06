from django.db import models
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    tanar = models.BooleanField(default=False)
    tanulo = models.BooleanField(default=False)

    def __str__(self):
        return self.username+' '+self.first_name

class CustomPolygon(models.Model):
    id = models.IntegerField(blank=False, auto_created=True, primary_key=True)
    name = models.CharField( max_length=255)
    geometry = models.TextField()
    leiras = models.TextField()
    letrehozo = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Territorie(models.Model):
    id = models.IntegerField(blank=False, auto_created=True, primary_key=True)
    name = models.CharField(max_length= 255, blank=True)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    color = models.CharField(max_length = 8)   
    geometry = models.TextField()

class Esemeny(models.Model):
    id = models.IntegerField(blank=False, auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    idopont = models.IntegerField()
    leiras = models.TextField()
    kep = models.ImageField(upload_to='test_geojson_store/files/uploads/esemenyek/', null=True)
    geometry = models.TextField()



class FileUpload(models.Model):
    
    

    file = models.FileField(upload_to='files/uploads/')
    