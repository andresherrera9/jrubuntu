from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/polls/<int:polls_id>/', views.index, name='polls'),
    
]