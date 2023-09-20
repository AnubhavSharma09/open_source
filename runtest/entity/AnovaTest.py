import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as spi
import statsmodels.stats.multicomp as multi 
from ..usecase.FilterExcelData import *

class OneWayAnova:
    def __init__(self,values,target,factor,flag):
        self.values=values
        self.target=target
        self.factor=factor
        self.flag=flag
    

    def CleanData(self):
         filtered_data=filter_data(self.values)
         data=filtered_data.filter_fileData()
         return data
       

    def Anova(self):
        self.values=pd.read_csv(self.values)
        self.values=self.values.rename({self.target:'target'},axis=1)
        testString='target' + '~' + 'C('+self.factor+',Sum)' 
        model= spi.ols(testString,data=self.values).fit()
        table = sm.stats.anova_lm(model, typ=2) 
        if self.flag=='true':
            c=self.post_hoc()
            return c
        return table
      

    def post_hoc(self):
        result=multi.MultiComparison(self.values['target'],self.values[self.factor])
        Results = result.tukeyhsd() 
        return Results._results_table
    
    def execute(self):
        return self.Anova()
        
    