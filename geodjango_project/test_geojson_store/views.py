from django.shortcuts import render
from .forms import TerritorieImportForm
from .models import Territorie
import json
from django.http.response import JsonResponse, HttpResponse
from .serializer import TerritorieSerializer
from rest_framework.decorators import api_view

# Create your views here.
def ImportTerritoriesFromJson(request):
    if request.method == "POST":
        form = TerritorieImportForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = request.FILES['file']
            try:   
                form.save()
                '''
                geojson_file = json.load(uploaded)
                json_array = geojson_file["features"]
                for item in json_array:
                    Territorie.objects.create(
                        name=item["properties"]["name"],
                        start_date=int(item["properties"]["start_date"]),
                        end_date=int(item["properties"]["end_date"]),
                        color=item["properties"]["color"],
                        geometry=item["geometry"]["coordinates"])
                return render(request, "upload_json.html", {"form" : form})'''
            except Exception as e:
                print("try->exception: "+str(e))
                return render(request, "upload_json.html", {"form" : form})
        return render(request, "upload_json.html", {"form" : form})    
    else:
        form = TerritorieImportForm()
        return render(request, "upload_json.html", {"form" : form})
    
def GetIndexPage(request):
    return render(request, 'index.html', status=200)

def post_UploadGeoJsonFile(request):
    if request.method == "POST":
        form = TerritorieImportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"feltoltes es mentes sikeres."})
        else:
            return JsonResponse({"message":"error: "+str(form.errors)}, status = 400)
    else:
        return JsonResponse({"message":"csak post metodus engedelyezett."}, status= 405)

@api_view(['GET'])
def get_TerritoriesAPI(request):
    territories = Territorie.objects.all()
    serialized = TerritorieSerializer(territories, many= True)
    return JsonResponse(serialized.data, safe=False)