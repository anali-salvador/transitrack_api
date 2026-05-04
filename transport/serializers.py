from rest_framework import serializers
from .models import Conductor, Ruta

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    conductor_nombre = serializers.CharField(source='conductor.nombre', read_only=True)
    
    class Meta:
        model = Ruta
        fields = '__all__'