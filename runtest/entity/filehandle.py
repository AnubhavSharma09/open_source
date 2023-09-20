from ..usecase.globalvar import filehandle_var

class filehandle:
    def __init__(self,f):
        self.f=f
 


    def write_file(self):
        filehandle_var['path']= str(self.f)
        with open(str(self.f), "wb+") as destination:
          for chunk in self.f.chunks():
              destination.write(chunk) 

        return True
        
    