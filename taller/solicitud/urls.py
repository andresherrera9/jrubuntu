from django.urls import path 
from . import views


urlpatterns = [
    path('solicitud2/',views.index_solicitud,name='index_solicitud'),
    path('',views.get_name,name='solicitud'),

    ]