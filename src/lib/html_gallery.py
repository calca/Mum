""" Build html page from thumb fir """

import os, math

import utils, html, constants, resize

class html_gallery(html.html):

    lista = utils.utility()

    def __init__(self,path_thumb=None,dir_img_html=None,row=None,col=None,tpl_page=None,tpl_thumb=None,title=None):
        """
        Create a web-gallery

        @type path_thumb:string
        @param path_thumb: path where store a img
        @type dir_img_html:string
        @param dir_img_html: dirname where are stored an html page
        @type row:int
        @param row: number of row for table
        @type  col:int
        @param col: number of columns for table
        @type  tpl_page:string
        @param tpl_page: file html for page
        @type  tpl_thumb:string
        @param tpl_thumb: file html for thumb
        @type  title:string
        @param title: title for webgallery
        """
        
        if path_thumb:
            self.set_path_thumb(path_thumb)
            
        if tpl_page:
            self.set_template_page(tpl_page)

        if tpl_thumb:
            self.set_template_thumb(tpl_thumb)

        if dir_img_html:
            self.set_html_dir(dir_img_html)

        if row:
            self.set_rows(row)

        if col:
            self.set_colums(col)
            
        if title:
            self.set_title(title)


    def set_path_thumb(self,uri):
        """
        Set path where store thumb
        @type uri:string
        @param uri: path where store a img
        """
        if os.path.isdir(uri):
            self.path_dest, self.dir_thumb,= os.path.split(uri)
            self.list_img=self.lista.list_img(uri)
            if not len(self.list_img):
                print 'html_gallery:: path_thumb havent image'
                return  0
            return 1
        return 0

    def set_template_page(self,uri):
        if os.path.isfile(uri):
            self.tpl_source = os.path.split(uri)[0]
            self.pag_index = self.load_page(uri)
            return 1
        return 0
    
    def set_template_thumb(self,uri):
        if os.path.isfile(uri):
            self.pag_thumb = self.load_page(uri)
            return 1
        return 0
    
    def set_html_dir(self,uri):
        """
        @type uri:string
        @param uri:dirname where are stored an html page
        """
        self.dir_img_html=uri
        
    def set_rows(self,number):
        self.row=number
        
    def set_colums(self,number):
        self.col=number
        
    def set_title(self,title):
        self.title=title
        
    def __build_menu(self):
        
        menu_thumb=''
        a= 0
        v_a = 0
        for x in range(self.numero_pagine):
            if not x:
                a = ''
            else:    
                a = x + 1
            v_a = x + 1 
            menu_thumb+='&nbsp&nbsp <a href='+constants.NAME_INDEX+'%s.html>Page %s</a> ' % ( a, v_a )
            
        return menu_thumb
            
    def __num_pagine(self):
        
        self.numero_pagine=math.ceil(int(len(self.list_img) / (self.row*self.col)))
        if (len(self.list_img) % (self.row*self.col)) > 0:
            self.numero_pagine += 1
        self.numero_pagine=int(self.numero_pagine)

    def __build_grid_thumb(self,lista):

        table = ''
        d= {}
        html = ''
        lista.reverse()
        for r in range(self.row):
            table+='<tr>'

            for c in range(self.col):
                if len(lista) > 0:
                    img = lista.pop()
                    d[constants.MUM_THUMBNAIL_LINK]=self.dir_img_html+'/'+img+'.html'
                    d[constants.MUM_THUMBNAIL_THUMB]='img src="'+self.dir_thumb+'/'+img+'"'
                    html = self.build_html(self.pag_thumb,d)
                table+='<td>'+html+'</td>'
                html=''
                
            table+='</tr>'

        return table
                
    def __build_page_thumb(self,lista,name_page,menu):

        d = {}
        d[constants.MUM_INDEX_TITLE]=self.title
        d[constants.MUM_INDEX_TABLE]=self.__build_grid_thumb(lista)
        d[constants.MUM_INDEX_MENU]=menu

        buffer = self.build_html(self.pag_index,d)
        self.write_page(buffer,os.path.join(self.path_dest,name_page))
        

    def build(self):
        # Controllo che le var siano inializzate
        if self.list_img and self.pag_thumb and self.pag_index  and self.row and self.col and self.path_dest and self.dir_img_html:
            
            self.__num_pagine()
            if self.numero_pagine == 1:
                self.__build_page_thumb(self.list_img,constants.NAME_INDEX+'.html','')
            else:
                menu=self.__build_menu()
                start = 0
                stop = self.row*self.col
                x = ''
                
                while start <= len(self.list_img):                
                    self.__build_page_thumb(self.list_img[start:stop],constants.NAME_INDEX+str(x)+'.html',menu)
                    start += self.row*self.col
                    stop += self.row*self.col
                    if x == '':
                        x=1
                        x += 1
                        
                        
            #copy image from template dir
            self.lista.copy_img(self.tpl_source,self.path_dest)
            
        else:
            return 0
            

if __name__ == '__main__':
    
    p = constants.IMAGE_SIZES
    thumb = resize.mthumb('paesaggi','prova/thumb',p[0])
    thumb.create()
    p = html_gallery('prova/thumb','resize-480x320',5,4,'../template/Classic/index.html','../template/Classic/thumbnail.html','pippunga titolo')
    p.build()
