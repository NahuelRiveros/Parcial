from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('', Home , name="home"),
    path('Organismos', api_Organismos , name="pi1"),
    path('Programas', api_Programas , name="pi2"),
    path('Museos', api_Museos , name="pi3"),
    path('Insitutos', api_Institutos , name="pi4"),
    path('Tramites', api_Tramites , name="pi5"),
    path('Convocatorias', api_Convocatorias , name="pi6"),
]