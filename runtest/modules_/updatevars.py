from ..usecase.globalvar import *



class test_update:
    def __init__(self,value):
        self.value=value

    def update_context(self):
        for i in range(len(self.value)-1):
             for j in range(len(self.value)-1):
                 if context[i]==self.value[j]:
                     context[i].append(self.value[j])
                 

