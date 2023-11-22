from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Cuest, Quizros, answ
import pandas as pd
from django.contrib import messages
import csv
from pathlib import Path
from django.utils import timezone
import pytz
from datetime import datetime
import sys

#¿Cambiar de staticfiles a static?

def index(request,polls_id,page_id):
    bogota_timezone = pytz.timezone('America/Bogota')
    current_time = datetime.now(bogota_timezone).strftime('%Y-%m-%d-%H:%M')
    print(current_time)
    polls_id = str(polls_id)
    idpage = page_id
    if request.method == 'POST':
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        print(data_)

        for x in data_:
            if '-MULTIPLE' in x or '-UNA' in x :
                p_total = int(x[-1])
                p_correctas = int(x[-3])
                count_t = data_[x].count("True")
                count_f = data_[x].count("False")
                n = (p_total / p_correctas)
                data_[x] = (n*(count_t) + n*(-(count_f))) / p_total 
                if data_[x] < 0:
                    data_[x] = 0
           
        path = Path('static/media/ROS_'+polls_id+'.csv')
        
        if path.is_file():
            df = pd.read_csv('static/media/ROS_'+polls_id+'.csv')
            df2 = pd.DataFrame(data_)
            df2["fecha"] = current_time
            for k,v in data_.items():
                df2[str(k)] = v         
                df2[str(k)] = df2[str(k)].replace({'True':1,'False':0})
                df_f = pd.concat([df,df2],ignore_index=True)
                df_f.to_csv('static/media/ROS_'+polls_id+'.csv', index=False)
        else:
            
            df = pd.DataFrame.from_dict(data_)
            df["fecha"] = current_time
            df.to_csv('static/media/ROS_'+polls_id+'.csv',index=False)

        messages.success(request,messages.INFO, 'Hola mundo')
        return redirect(request.path)
            
    else:
        questions = Cuest.objects.filter(quizros_id = polls_id)
        pdf_vinculos = "ANEXOROS"+str(idpage)+".pdf"
        print(pdf_vinculos) 
        context = {'questions':questions,'idpage':idpage,'pdf_vinculos':pdf_vinculos}
        
        return render(request,'polls/basic.html',context)

  
