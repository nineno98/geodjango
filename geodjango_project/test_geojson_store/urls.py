from django.urls import path
from .views import ImportTerritoriesFromJson, GetIndexPage, post_UploadGeoJsonFile, get_TerritoriesAPI, get_home, bejelentkezes, kijelentkezes

urlpatterns = [
    path('importjson/', view=ImportTerritoriesFromJson, name='importterritoriejson'),
    path('index/', name='index', view=GetIndexPage),
    path('territories_upload_POST/', view=post_UploadGeoJsonFile, name='post_UploadGeoJsonFile'),
    path('get_territories/', view=get_TerritoriesAPI, name='get_territories_api'),
    path('home/', view=get_home, name='home'),
    
    path('login/', view=bejelentkezes, name='login'),
    path('logout/', view=kijelentkezes, name='logout')

    
]