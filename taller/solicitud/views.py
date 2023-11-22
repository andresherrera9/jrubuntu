from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import NameForm, solicitudForm





def index_solicitud(request):
    
    return render(request,'solicitud/base_solicitud.html')

def get_name(request):

    if request.method == 'POST':

        form = solicitudForm(request.POST)

        if form.is_valid():

            #return HttpResponse("gracias!")
            pass

    else:
            
        form = solicitudForm()

    return render(request, 'solicitud/solicitud.html',{'form':form})
