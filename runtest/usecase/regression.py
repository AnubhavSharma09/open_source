from ..entity.forms import UploadFileForm,handle_uploaded_file,read_data
from .globalvar import context,filehandle_var,features
from .readExceldata import generate_data
from ..entity.filehandle import filehandle

import threading as td
import multiprocessing as mp
from django.http import HttpResponseRedirect,JsonResponse
# Create your views here.
from django.http import HttpResponse
import pandas as pd




class regression_test:
    def __init__(self):
        pass

    def conduct_test(self):
            a=generate_data()
            child_conn, parent_conn = mp.Pipe()
            data=pd.read_csv(filehandle_var['path'])
            prcs=mp.Process(target=a.generate,args=(parent_conn,data))
            prcs.start()
            lst=[]
            lst=child_conn.recv()
            context['correlation'].append(lst['correlation'])
            context['median'].append(lst['median'])
            context['residual'].append(lst['residual']) 
            context['min'].append(lst['min'])  
            context['1q'].append(lst['1q']) 
            context['3q'].append(lst['3q']) 
            context['max'].append(lst['max']) 
            context['Y'].append(lst['Y']) 
            context['stderr'].append(lst['stderr'])
            context['tstat'].append(lst['tstat'])  
            context['p_value'].append(lst['p_value'])  
            prcs.join()
            prcs.close() 
            return  JsonResponse({'median':str(context['median']),
                                        'min':str(context['min']),
                                        'residual':str(context['residual']),
                                        'correlation':str(context['correlation']),
                                        '1q':str(context['1q']),
                                        '3q':str(context['3q']),
                                         'max':str(context['max']),'Y':str(context['Y']),
                                        'stderr':str(context['stderr']),
                                          'tstat':str(context['tstat']),
                                          'p_value':str(context['p_value'])
                                         })