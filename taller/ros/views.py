from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import textros
from pathlib import Path
from os.path import exists



def index_ros(request, page_id,ros_id):

    ide=str(ros_id)
    idpage = page_id
    url = '/ROS'+ide +'.pdf'
    url_anexo = '/ANEXOROS'+ide +'.pdf'
    url_exists = exists('ros/static/ROS'+ide +'.pdf') # al pasar al despliegue puede que esto falle, cambiar ruta al estatico general
    anexo_exists = exists('ros/static/ANEXOROS'+ide +'.pdf') # al pasar al despliegue puede que esto falle, cambiar ruta al estatico general
    print(url_exists)
    print(anexo_exists)

    return render(request, 'ros/detail.html', {'url':url,'url_anexo':url_anexo,
                                              'ide':ide,'idpage':idpage,'url_exists':url_exists,'anexo_exists':anexo_exists})

                                              