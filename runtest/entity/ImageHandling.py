from PIL import Image
import io
import os


class CreateImage:
    def __init__(self,fig):
        self.fig=fig


    def create_img_path(self,path):
         if os.path.exists('./runtest/static/'+path.rstrip('.csv'))==False:
                 os.mkdir('./runtest/static/'+path.rstrip('.csv'))
                 return True
         return True

    def saveImage(self,path,name):
        error=BufferError()
        buf = io.BytesIO()
        self.fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        if self.create_img_path(path)==True:
               img.save('./runtest/static/'+path.rstrip('.csv')+'/'+name+'.png')
               img.close()
               return  '/'+path.rstrip('.csv')+'/'+name+'.png'
        img.close()
        return error.add_note('Error Saving Image. Check path')
    