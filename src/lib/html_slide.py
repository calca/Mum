""" Build html page from thumb dir """

import os, math
import Image

import utils, html, constants, resize, html_gallery


class html_slide(html.html):

    lista = utils.utility()

    def __init__(self,path_size=None,path_store_html=None,dir_thumb=None,tpl_page=None,title=None):
        """
        Create a web-slide
        
        @type path_size:string
        @param path_size: path where are stored image
        @type path_store_html:string
        @param path_store_html: path where put html page
        @type dir_thumb:string
        @param dir_thumb: dirname where are stored a thumb img
        @type  tpl_page:string
        @param tpl_page: file html for page
        @type  title:string
        @param title: title for webgallery
        """
        
        # import web-related file formats
        import GifImagePlugin
        import JpegImagePlugin
        import PngImagePlugin

        # don't look for more plugins
        Image._initialized = 1

        if path_size:
            self.set_path_size(path_size)

        if path_store_html:
            self.set_path_store_html(path_store_html)

        if dir_thumb:
            self.set_dir_thumb(dir_thumb)
            
        if tpl_page:
            self.set_template_page(tpl_page)

        if title:
            self.set_title(title)
        
    def set_template_page(self,value):
        if not os.path.isfile(value):
            print 'html_slide::set_template_page() value is not page'
            return False
        self.tpl_source, a = os.path.split(value)
        self.pag_slide = self.load_page(value)
        return True
    
    def set_path_size(self,value):
        if not os.path.isdir(value):
            print 'html_slide:: path_size is not dir'
            return False
        self.list_img=self.lista.list_img(value)
        if len(self.list_img) == 0:
            print 'html_slide:: path_size havent image'
            return False
        self.path_size = value
        a, self.dir_size = os.path.split(value)
        return True
        
    def set_path_store_html(self,value):
        if not os.path.isdir(value):
            os.mkdir(value)
        self.path_store_html = value
        
    def set_dir_thumb(self,value):
        self.dir_thumb = value
        
    def set_title(self,title):
        self.title=title
        
    def __build_page(self,title,file_name,img,
                     pre_link,next_link,
                     img_id,num_img,page_index,
                     pre_img,next_img,
                     comments,img_dim,file_size,save_page):
        d = {}
 
        d[constants.MUM_IMAGE_TITLE]=title + ' - ' + file_name
        d[constants.MUM_IMAGE_IMG_LINK_PRE]=pre_link
        d[constants.MUM_IMAGE_IMG_ID]=str(img_id)
        d[constants.MUM_IMAGE_IMG_N]=str(num_img)
        d[constants.MUM_IMAGE_IMG_LINK_NEXT]=next_link
        d[constants.MUM_IMAGE_PAGE_INDEX]=page_index
        d[constants.MUM_IMAGE_IMG_PREV]=pre_img
        d[constants.MUM_IMAGE_IMG]=img
        d[constants.MUM_IMAGE_IMG_NEXT]=next_img
        d[constants.MUM_IMAGE_COMMENTS]=comments
        d[constants.MUM_IMAGE_FILE_NAME]=file_name
        d[constants.MUM_IMAGE_IMG_DIM]=img_dim
        d[constants.MUM_IMAGE_FILE_SIZE]=file_size

        buffer = self.build_html(self.pag_slide,d)
        self.write_page(buffer,save_page)
        

    def build(self):
        idx = 0
        num_img = len(self.list_img)
        comments=''
        img_dim=''
        time=''
        while idx < num_img:
            pre_link=self.list_img[idx-1]+'.html'
            pre_img ='../'+self.dir_thumb+'/'+self.list_img[idx-1]
            next_idx = idx + 1
            if next_idx <  num_img:
                next_link=self.list_img[next_idx]+'.html'
                next_img='../'+self.dir_thumb+'/'+self.list_img[next_idx]
            else:
                next_link=self.list_img[0]+'.html'
                next_img='../'+self.dir_thumb+'/'+self.list_img[0]

            # info
            image=os.path.join(self.path_size,self.list_img[idx])
            im = Image.open(image)
            img_dim = " %s x %s " % im.size
            #exif
            self.__build_page(self.title,self.list_img[idx],'../'+self.dir_size+'/'+self.list_img[idx],
                              pre_link,next_link,
                              idx+1,num_img,'../'+constants.NAME_INDEX+".html",
                              pre_img,next_img,
                              comments,img_dim,time,os.path.join(self.path_store_html,self.list_img[idx]+'.html'))
            idx +=1
        #copy image from template dir
        self.lista.copy_img(self.tpl_source,self.path_store_html)


if __name__ == '__main__':
    
    p = constants.IMAGE_SIZES
    thumb = resize.mthumb('paesaggi','prova/thumb',p[0])
    thumb.create()
    thumb = resize.mthumb('paesaggi','prova/size-640x480',p[1])
    thumb.create()
    p = html_gallery.html_gallery('prova/thumb','html',5,4,'../template/Classic/index.html','../template/Classic/thumbnail.html','pippunga titolo')
    p.build()
    b = html_slide('prova/size-640x480','prova/html','thumb','../template/Classic/image.html','pippunga titolo');
    b.build()
