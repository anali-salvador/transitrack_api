from rest_framework.routers import DefaultRouter
from .views import ConductorViewSet, RutaViewSet

router = DefaultRouter()
router.register(r'rutas', RutaViewSet, basename='ruta')
router.register(r'conductores', ConductorViewSet, basename='conductor')

urlpatterns = router.urls