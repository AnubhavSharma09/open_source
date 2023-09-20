import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import csv
import threading as th
from PIL import Image
import io
from sklearn import linear_model

import numpy as np
from ..modules_.statsticaldata import create_statastical_inf
from .globalvar import filehandle_var,context
import multiprocessing as mp
import time
import random
import statsmodels.api as sm
import os 
from ..entity.ImageHandling import *
from ..usecase.FilterExcelData import *

lst_2={
    
    "correlation":[],
      "median":[],
      "residual":[],
       "min":[],
       "1q":[],
       "3q":[],
       "max":[],
       "intercept":0,
       "coef":0,
       "stderr":[],
       "Y":[],
       "tstat":[],
       "p_value":[],
       "pathregr":"",
       "path":""
}
    
lstofHeader=[]


class plot_gaphs:
    lstofHeader=[]
    def __init__(self,data,path):
        self.data=pd.read_csv(data)
        self.path=path
    
        

    def scatter(self):
        a=filter_data(self.path)
        lstofHeader=a.filter_fileData()
       
        plt.scatter(self.data[lstofHeader[0]],self.data[lstofHeader[1]])
        fig=plt.gcf()
        img= CreateImage(fig)
        imgPath=img.saveImage(self.path,'scatter')
        lst_2['path']=imgPath
        plt.clf() 


    
    def regression(self,parentprocess):
        regr= linear_model.LinearRegression()
        a=filter_data(self.path)
        lstofHeader=a.filter_fileData()
        s=np.reshape(self.data[lstofHeader[1]],(-1,1))
        k=np.reshape(self.data[lstofHeader[0]],(-1,1))
        regr.fit(k,s)
        df=sm.add_constant(k)
        result=sm.OLS(s,df).fit()
        y_predict=regr.predict(k)
        plt.scatter(self.data[lstofHeader[0]],self.data[lstofHeader[1]],color="red")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.plot(k,y_predict)
        fig=plt.gcf()
        img= CreateImage(fig)
        imgPath=img.saveImage(self.path,'Regression')
        plt.clf()
        lst_2['pathregr']=imgPath
        a=generate_data()
        a.generate(parentprocess,self.data,self.path)
       
      


   
 

  
class generate_data:
    def __init__(self):
         pass

    
    def generate(self,parent_conn,data,path):
                regr= linear_model.LinearRegression()
                a=filter_data(path)
                lstofHeader=a.filter_fileData()
                regr= linear_model.LinearRegression() 
                s=np.reshape(data[lstofHeader[1]],(-1,1))
                k=np.reshape(data[lstofHeader[0]],(-1,1))
                regr.fit(k,s)
                df=sm.add_constant(k)
                result=sm.OLS(s,df).fit()
                y_predict=regr.predict(k)
                df=pd.DataFrame({'actual':s.flatten(),'predicted':y_predict.flatten()})
                residual=np.sum(np.square(df['actual']-df['predicted']))
                y=residual/(len(s)-2)
               
                u=np.sqrt(y)
                q=random.random()
                r=create_statastical_inf(s)
                lst_2['correlation']=result.rsquared
                lst_2['1q']=r.find_q_1()
                lst_2['3q']=r.find_q_3()
                lst_2['median']=r.find_median()
                lst_2['residual']=result.mse_resid
                lst_2['max']=r.max()
                lst_2['mean']=r.find_mean()
                lst_2['intercept']=result.params[0]
                lst_2['coef']=result.params[1]
                lst_2['Y']=result.params[1]
                lst_2['tstat']=result.tvalues[1]
                lst_2['tvalinter']=result.tvalues[0]
                lst_2['pvalinter']=result.pvalues[0]
                lst_2['p_value']=result.pvalues[1]
                lst_2['intercepterr']=result.bse[0]
                lst_2['stderr']=result.bse[1]
                lst_2['df']=len(s)-2
                lst_2['fstat']=result.fvalue                 
                parent_conn.send(lst_2)
                

  
