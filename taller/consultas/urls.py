from django.urls import path
from . import views

urlpatterns = [
    path('consultas/',views.index, name='index'),
    path('consultas/resultado_persona/<int:idpage>/', views.resultado_persona, name='resultado_persona'),
    path('consultas/resultado_persona/vistas/', views.vistas, name='vistas'),
]