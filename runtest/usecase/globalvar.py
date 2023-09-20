import os
import array
import sys

#sample variables


counterlst=[]
filehandle_var = {
    "path":""
}
context = {
         
    
      "pathline":"line.png",
      "pathregr": "/" + filehandle_var['path']+"/regression.png",
      "data":"Home Page",
      "correlation":[],
      "median":[],
      "residual":[],
       "min":[],
       "1q":[],
       "3q":[],
       "max":[],
       "Y":[],
       "stderr":[]
    }



features = [

           'Regression',
           'One Way Anova',
           'Two Way Anova',
           'Variance',
           'Standard Deviation',
           'Quantile Deviation',
           'Critical Region' ,
           'Formulae',
           'Manova',
           'Chi-Sqaure',
           'P-value Test',
           'Two-Tail Test',
           'One-Tail Test'

           ]


lst_2={

    "correlation":[],
      "median":[],
      "residual":[],
       "mean":[],
       "1q":[],
       "3q":[],
       "max":[],
}


process_list=[]

filteredData=[]