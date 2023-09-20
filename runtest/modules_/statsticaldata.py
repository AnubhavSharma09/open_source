import statistics as stats
from ..usecase.globalvar import context
import numpy as np
from scipy.stats import sem
from sklearn.metrics import mean_squared_error
import scipy.stats
import math


class create_statastical_inf:
    def __init__(self,values):
        self.values=values

    def find_median(self):
        return str(stats.median(self.values))
    
    def find_mean(self):
           a= np.sum(self.values)/len(self.values)
           return str(a)

    def find_q_1(self):
         return str(np.quantile(self.values,0.25))
    
    def find_q_3(self):
         return str(np.quantile(self.values,0.75))
    
    def max(self):
         return str(np.max(self.values))
    
    def standard_error(self):
          return str(sem(self.values))
    
    def tstat(self,q):
          self.a=q/sem(self.values)
          return str(self.a)
    
    def interceptStandardError(self,a,y_predic):
       yi=y_predic
       xi=a
       n=len(y_predic)
       y_bar = sum(yi) / n
       x_bar = sum(xi) / n
       sum_residuals_squared = sum([(y - y_bar)**2 for y in yi])
       numerator_term1 = np.sqrt(sum_residuals_squared / (n - 2))
       sum_x_deviations_squared = sum([(x - x_bar)**2 for x in xi])
       second_term = np.sqrt(((1/n) + (x_bar**2)) / sum_x_deviations_squared)
       result = numerator_term1 * second_term
       return result
         
   
    
    def P_value(self):
         self.s=scipy.stats.t.sf(abs(self.a),len(self.values)-2)*2
         return self.s
         
    
    def fstat(self,a,y_predic):
         v=a/(len(self.values)-2)
         s=mean_squared_error(self.values,y_predic)
         return v/s
    
    def analyse(self,q):
         s=scipy.stats.t.sf(abs(self.a),len(self.values)-2)*2
         f=q/sem(self.values)
         if(s>f):
              return True
         else:
              return False