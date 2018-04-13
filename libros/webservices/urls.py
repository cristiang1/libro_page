from django.urls import path, include 
from rest_framework import routers
from home.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'Libro', libro_viewset)
router.register(r'Autor', autor_viewset)
router.register(r'Genero', genero_viewset)
router.register(r'Editorial', editorial_viewset)


urlpatterns = [
path('api/', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]