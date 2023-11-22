from django.urls import path 
from . import views
urlpatterns = [
    path('<int:page_id>/ros/<int:ros_id>/',views.index_ros,name='index_ros')
,]