from ..entity.AnovaTest import  OneWayAnova

listOfFunctions={'One Way Anova':OneWayAnova}

class ManageFunction:
    def __init__(self,values,ClassName,factor,target,flag):
        self.ClassName=ClassName
        self.factor=factor
        self.target=target
        self.flag=flag
        self.values=values

    def Call_Function(self):
        derivedClass=listOfFunctions.get(self.ClassName,0)
        functionValue=derivedClass(self.values,self.factor,self.target,self.flag)
        returnedValues=functionValue.execute()
        return returnedValues

        
        