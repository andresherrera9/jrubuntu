from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:results_id>/<str:start_date>/<str:end_date>/',views.getresults, name='getresults'),
    path('<int:results_id>/ind/',views.uniqueres, name='unique'),
]
