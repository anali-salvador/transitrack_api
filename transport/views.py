from rest_framework import viewsets, filters
from .models import Conductor, Ruta
from .serializers import ConductorSerializer, RutaSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['origen', 'destino']