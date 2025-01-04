from django import forms
from .models import Territorie
import json

class EsemenyImportForm(forms.Form):
    file = forms.FileField()

    def clean(self):
        cleaned_data = super().clean()
        uploaded_file = cleaned_data.get('file')
        if uploaded_file:
            try:
                json.load(uploaded_file)
                uploaded_file.seek(0)
            except json.JSONDecodeError:
                raise forms.ValidationError("A feltöltött GeoJSON fájl formátuma hibás!")
            except Exception as e:
                raise forms.ValidationError(f"Valami hiba történt: {str(e)}")
        return cleaned_data
    
    def save(self):
        uploaded = self.cleaned_data.get("file")


class TerritorieImportForm(forms.Form):

    file = forms.FileField()

    def clean(self):       
        cleaned_data = super().clean()
        uploaded_file = cleaned_data.get("file")
        if uploaded_file:
            try:
                # A fájl tartalmának beolvasása és JSON validálás
                json.load(uploaded_file)
                uploaded_file.seek(0)
            except json.JSONDecodeError:
                raise forms.ValidationError("A feltöltött GeoJSON fájl formátuma hibás!")
            except Exception as e:
                raise forms.ValidationError(f"Valami hiba történt: {str(e)}")
        return cleaned_data
    
    def save(self):
        uploaded = self.cleaned_data.get("file")
        try:
            geojson_data = json.load(uploaded)
            json_array = geojson_data["features"]
            for item in json_array:
                Territorie.objects.create(
                    name=item["properties"]["name"],
                    start_date=int(item["properties"]["start_date"]),
                    end_date=int(item["properties"]["end_date"]),
                    color=item["properties"]["color"],
                    geometry=item["geometry"]["coordinates"]
                )
        except Exception as e:
            pass
