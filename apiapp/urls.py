from django.urls import path, include
from .views import *
from rest_framework import routers


#DEFINE RUTA DEL API
router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('tipoproducto', TipoProductoViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]