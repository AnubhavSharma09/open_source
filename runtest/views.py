from django.shortcuts import render
from django.template import loader,Template,Context
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .entity.forms import UploadFileForm,handle_uploaded_file,read_data
from .usecase.globalvar import context,filehandle_var,features
from .usecase.readExceldata import generate_data
from .entity.filehandle import filehandle
from .entity.AnovaTest import OneWayAnova
import json
from .controller.manageFunctions import ManageFunction

import threading as td
import multiprocessing as mp

# Create your views here.
from django.http import HttpResponse
import pandas as pd
from .usecase.regression import regression_test

import sys

prcs_lst=[]
functionsd=['One Way Anova','Regression','TwoWayAnova','MultiLinearRegression']

def index(request):
    template = loader.get_template('runtest/index.html')
   
    return HttpResponse(template.render())

def apppage(request):
    template_1 = loader.get_template('runtest/apppage.html')
    context['data']='Home'
    return render(request,'runtest/maintemplate.html',context)


def onewayanova(request):
    template_1 = loader.get_template('runtest/maintemplate.html')
    context['data']='One Way Anova'
    return render(request,'runtest/maintemplate.html',context)


def regressions(request):
     context['data']='Regression'
     return render(request,'runtest/maintemplate.html',context)


def retests(request):
    for i in range(len(features)-1):
      if features[i]==context['data']:    
         a=regression_test()
         return a.conduct_test()
      else:
         return HttpResponse("value")
          
         
@csrf_exempt
def test_data(request):
    recvValues=json.loads(request.body.decode())
    factor=recvValues['factor']
    flag=recvValues['flag']
    target=recvValues['target']
    calledClass=ManageFunction(filehandle_var['path'],context['data'],target,factor,flag)
    function=calledClass.Call_Function()
    if flag=="true":
         return JsonResponse(json.dumps(str(function)),safe=False)
             
    return JsonResponse(function.to_json(),safe=False)
  

@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        child_conn, parent_conn=mp.Pipe()
        f=filehandle(request.FILES["File"])
        if f.write_file()==True:
            prcs= mp.Process(target=handle_uploaded_file,args=(filehandle_var['path'],parent_conn,context['data']))
            prcs.start()
            lst = child_conn.recv()
            context.update(lst)
            prcs.join()
            prcs.close()
            string=context['data']
            context['data']=string.replace(" ","")
        return HttpResponseRedirect("/apppage/home/" + context['data']) 
    else:
        form = UploadFileForm(request.POST, request.FILES)
    return HttpResponse(request)


