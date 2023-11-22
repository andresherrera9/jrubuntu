from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd
import csv
import json




def getresults(request,results_id,start_date,end_date):
    start_date = datetime.strptime(start_date,'%Y-%m-%d-%H:%M')
    end_date = datetime.strptime(end_date,'%Y-%m-%d-%H:%M')
    results_id = str(results_id)
    df = pd.read_csv('static/media/ROS_'+results_id+'.csv')
    #df = df.fillna(0)
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d-%H:%M')
    df = df[(df['fecha'] >= start_date) & (df['fecha'] <= end_date)]
    df = df[df.columns[df.columns.str.contains('-MULTIPLE|-UNA')]]
    df.loc['Total'] = (df.sum(numeric_only=True,axis=0) / len(df))
    df = df.iloc[[-1]]
    df = df.rename(columns=lambda x: x.split('-ROS')[0] if '-ROS' in x else x)
    
    #---code to render graphs with javascript library---#

    ques_list = df.columns.tolist()
    #print(ques_list[0])
    ques_range = range(len(ques_list))
    res_list = df.iloc[0].tolist()
    res_list_all = res_list


    return render(request,'results/barchart.html',{"ques_list":ques_list, "res_list":res_list[0],"res_list_all":res_list_all,"ques_range":ques_range})


def uniqueres(request,results_id):
    results_id = str(results_id)
    df = pd.read_csv('static/media/ROS_'+results_id+'.csv')
    df = df.fillna(0)
    geeks_object = df.to_html()
  
    return HttpResponse(geeks_object)



