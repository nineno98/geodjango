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
    geometry = models.TextField()



class FileUpload(models.Model):
    
    fs = FileSystemStorage(location="files/uploads")

    file = models.FileField(storage=fs)
    def save(self, *args, **kwargs):
        geojson_file = json.load(self.file)
        json_array = geojson_file["features"]
        for item in json_array:
            Territorie.objects.create(
                name=item["properties"]["name"],
                start_date=int(item["properties"]["start_date"]),
                end_date=int(item["properties"]["end_date"]),
                color=item["properties"]["color"],
                geometry=item["geometry"]["coordinates"]
            )
        #print(geojson_file["features"][0])
        return super(FileUpload, self).save(*args, **kwargs)