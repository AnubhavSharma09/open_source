import pandas as pd
import numpy as np

class filter_data:
    def __init__(self,fileptr):
        self.fileptr=fileptr
    


    def filter_fileData(self):
        csvFile=pd.read_csv(self.fileptr)
        IndexName=csvFile.columns
        return IndexName


        
        