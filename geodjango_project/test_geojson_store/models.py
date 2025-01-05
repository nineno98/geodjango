from django.db import models
from django.core.files.storage import FileSystemStorage
import json

# Create your models here.



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
    