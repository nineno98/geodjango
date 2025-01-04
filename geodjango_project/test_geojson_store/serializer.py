from rest_framework import serializers
from .models import Territorie

class TerritorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Territorie
        fields = '__all__'
        depth = 1
    