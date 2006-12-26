""" A simple class for generating thumb  """

import Image, os, re

import constants, utils


class mthumb:
   
    def __init__(self,path_img=None,path_dest=None,size=None):
        """
        Create a thumb from path where store images

        @type  path_img: string
        @param path_img: path where stored images
        @type  path_dest: string
        @param path_dest: The directory where the had resized files will be saved.
       
        """

        self.id=0
       
        # import web-related file formats
        import GifImagePlugin
        import JpegImagePlugin
        import PngImagePlugin
        
        # don't look for more plugins
        Image._initialized = 1
        
        if path_img:
            self.set_path_img(path_img)
            self.pi_ok=1
            
        if path_dest:
            self.set_path_dest(path_dest)
            self.pd_ok=1
            
        if size:
            self.size=size
            self.si_ok=1
            
        return
    
    def set_path_img(self,value):
        
        """
        Set path where is stored images
        
        @type  value: string
        @param value: path where stored images
        """
        
        if os.path.isdir(value):
            self.path_img=value
            obj=utils.utility()
            self.lista=obj.list_img(self.path_img)
            self.pi_ok=1
        else:
            print "resize::init: path_img is not a dir"

    def set_path_dest(self,value):
        """
        Set path where put images resized

        @type  value: string
        @param value: The directory where the had resized files will be saved.
        """
        if os.path.isdir(value):
            self.path_dest=value
        else:
            os.mkdir(value)
            self.path_dest=value
            
        self.pd_ok=1

    def set_size(self,value):
        """
        Set size of resized images
        
        @type  value: IMAGE_SIZE
        @param value: size of thumb
        """
        self.size=value
        self.si_ok=1
        
    def __build_image(self,image,thumb,size):
        """
        Create a thumb for image

        @type image: string
        @param image: image path
        @type  thumb: string
        @param thumb: thumb path
        @type  size: IMAGE_SIZE
        @param size: size of thumb
        """
        try:
            im = Image.open(image)
            im.thumbnail(size)
            im.save(thumb)
            return 1
        except:
            return 0

    def __check_param(self):
        if not self.pi_ok:
            print "resize:: path_img isn't set"
            return 0
        if not self.pd_ok:
            print "resize:: path_dest isn't set"
            return 0
        if not self.si_ok:
            print "resize:: size isn't set"
            return 0
        
        #ok check
        return 1
    
    def next(self):
        
        if not self.__check_param():
            return 0
        
        if self.id >= len(self.lista):
            return 0
        
        self.__build_image(os.path.join(self.path_img,self.lista[self.id]),
                           os.path.join(self.path_dest,self.lista[self.id]),
                           self.size)
        self.id+=1
        return 1
    
    def create(self):
        while self.next():
            pass
        return

    
if __name__ == '__main__' :

    p = constants.IMAGE_SIZES
    thumb = mthumb('paesaggi','prova/thumb',p[0])
    thumb.create()
    
