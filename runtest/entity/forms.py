from django import forms
from ..usecase.readExceldata import plot_gaphs
import multiprocessing as prcs
from ..usecase.globalvar import context,filehandle_var
from .filehandle import *
import threading as td
from ..usecase.FilterExcelData import *
from django.http import HttpResponseRedirect,JsonResponse


result=[]
functionsd=['OneWayAnova','Regression','TwoWayAnova','MultiLinearRegression']
lst={
              'Factor_1':[]
           }



def functionClear(string):
      newString=string.replace(" ","")
      return newString

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50) 
    file = forms.FileField()


def read_data(path,prcss,func):
     filtered_data=filter_data(path)
     data=filtered_data.filter_fileData()
 
     if func==functionsd[0]:
           for i in range(0,len(data)):
               lst['Factor_1'].append(data[i])
           prcss.send(lst)
           return True
     elif func==functionsd[1]:
            print('Initialising Regression Test')
            a=plot_gaphs(path,path)
            a.scatter()
            a.regression(prcss)
           
    



def handle_uploaded_file(f,prcss,functionName):
            for i in range(len(functionsd)):
               if functionClear(functionName)==functionsd[i]:
                   read_data(f,prcss,functionsd[i])
  
 
 
    
 

 
  