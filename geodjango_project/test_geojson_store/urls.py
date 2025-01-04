from django.urls import path
from .views import ImportTerritoriesFromJson, GetIndexPage, post_UploadGeoJsonFile, get_TerritoriesAPI

urlpatterns = [
    path('importjson/', view=ImportTerritoriesFromJson, name='importterritoriejson'),
    path('index/', name='index', view=GetIndexPage),
    path('territories_upload_POST/', view=post_UploadGeoJsonFile, name='post_UploadGeoJsonFile'),
    path('get_territories/', view=get_TerritoriesAPI, name='get_territories_api')
    
]