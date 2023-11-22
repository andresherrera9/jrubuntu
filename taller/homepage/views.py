from django.shortcuts import render
from django.http import HttpResponse




def homepage(request):
    return render(request,'homepage/homepage.html')

def homepage2(request,page_id):
    print(page_id)
    return render(request,'homepage/homepage2.html')