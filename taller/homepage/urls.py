from django.conf.urls import url, include
from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('<int:page_id>/', views.homepage2, name='homepage2'),
]