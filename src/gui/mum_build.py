"""
Mum thread that create a gallery and
upload on website
"""
## /*
##  *             ,           , 
##  *	         /             \ 
##  *		((__-^^-,-^^-__)) 
##  *		`-_---' `---_-' 
##  *		 `--|o` 'o|--' 
##  *		    \  `  / 
##  *		     ): :( 
##  *		     :o_o: 
##  *		      "-" 
##  *	
##  *  This program is free software; you can redistribute it and/or modify
##  *  it under the terms of the GNU General Public License as published by
##  *  the Free Software Foundation; either version 2 of the License, or
##  *  (at your option) any later version.
##  *
##  *  This program is distributed in the hope that it will be useful,
##  *  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  *  GNU Library General Public License for more details.
##  *
##  *  You should have received a copy of the GNU General Public License
##  *  along with this program; if not, write to the Free Software
##  *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##  *
##  *  Copyright 2004 Calcaterra Gianluigi <gianluigi.calcaterra@tin.it>
##  *
##  */




import gtk

import os, socket, ftplib, time
from threading import Thread

import label
from lib.utils import utility
from lib.resize import mthumb
from lib.html_gallery import html_gallery
from lib.html_slide import html_slide
from lib.update_ftp import update_ftp, Finder, no_dir_ftp
from lib.update_ftp_index import update_ftp_index
from lib import constants

        
class mum_build(Thread):

    def __init__(self,parent,progressbar,statusbar,id_status):
        Thread.__init__(self)
        self.parent=parent
        self.progressbar=progressbar
        self.statusbar=statusbar
        self.id_status=id_status
        self.enable_web = False
        self.enable_update_index = False
        self.enable_upload_only = False

        # in caso di rootdir
        self.path_ftp=""

        # controllo thread
        self.__suspende_flag = False
        self.__end_flag = False
        self.__have_error = False

        # controlo status bar
        self.__status=0
        
    def suspende_thread(self):
        self.__suspende_flag = True

    def resume_thread(self):
        self.__suspende_flag = False

    def terminate(self):
        self.resume_thread()
        self.__end_flag = True

    def set_theme(self,theme):
        self.theme=theme

    def set_resolution(self,resolution):
        self.resolution=resolution+1
        
    def set_title_album(self,title_album):
        self.title_album=title_album

    def set_source_album(self,source_album):
        self.source_album=source_album

    def set_dest_album(self,dest_album):
        self.dest_album=dest_album

    def set_web_url(self,web_url):
        self.WebUrl = web_url

    def set_web_login(self,web_login):
        self.WebLogin = web_login

    def set_web_password(self,web_password):
        self.WebPassword = web_password

    def set_web_rootdir(self,web_rootdir):
        self.path_ftp=web_rootdir

    def set_enable_web(self):
        self.enable_web = True

    def set_enable_update_index(self):
        self.enable_update_index = True

    def set_enable_upload_only(self):
        self.enable_upload_only = True

    def get_response(self):
        return self.__ok

    def __num_op(self):
        # numero di operazione 
        op_u = utility().count_img(self.source_album)
        op = op_u*2
        op += 3
        if self.enable_web:
            op += op_u*3
            op += 30 #upload
        return op

    def __attendi(self):
        while self.__suspende_flag:
            time.sleep(1.0)

        if self.__end_flag:
            self.__end_thread()
            return False
            
        return True

    def __error(self,error):
        self.__value_error=error
        self.__have_error= True
        self.terminate()
        self.__set_status_bar(error)
        gtk.threads_enter()
        self.statusbar.pop(self.id_status)
        gtk.threads_leave()

    def __set_status_bar(self,messaggio):
        gtk.threads_enter()
        if self.__status > 0:
            self.statusbar.pop(self.__status)
        self.__status  = self.statusbar.get_context_id("2")
        self.statusbar.push(self.__status,messaggio)
        gtk.threads_leave()
        
           
    def have_error(self):
        return self.__have_error

    def get_error(self):
        return self.__value_error;
    

    def __end_thread(self):

        if not self.have_error():
            self.__set_status_bar(label.MUM_STOP_OPERATION)
   
        return True
    
    def run(self):
        self.total = self.__num_op()
        self.count = 0.0

        if not self.enable_upload_only: 
            if self.__attendi():
                self.__create_thumb()
                if self.__attendi():
                    self.__resize()
                    if self.__attendi():
                        self.__build_html()
                        
        if self.__attendi():
            self.__upload_gallery()
            if self.__attendi():                                     
                self.__update_index()

        # Stop Thread
        if self.__end_flag:
            self.__end_thread()
            return False
            
        # Corretta
        self.__set_status_bar(label.MUM_COMPLETED_OPERATION)
        gtk.threads_enter()
        self.progressbar.set_fraction(1.0)
        self.statusbar.pop(self.id_status)
        gtk.threads_leave()
        return True
        
    def __create_thumb(self):
        # create thumb
        self.__set_status_bar(label.MUM_PROGDIALOG_THUMB)
        gtk.threads_enter()
        self.progressbar.set_fraction(self.count/self.total)
        gtk.threads_leave()
        thumb = mthumb(self.source_album,
                       os.path.join(self.dest_album,constants.DIR_THUMB),
                       constants.IMAGE_SIZES[0])
        while self.__attendi() and thumb.next():
            gtk.threads_enter()
            self.progressbar.set_fraction(self.count/self.total)
            gtk.threads_leave()
            self.count +=1
            
    def __resize(self):
        # rezise image
        self.__set_status_bar(label.MUM_PROGDIALOG_IMAGE)
        gtk.threads_enter()
        gtk.threads_leave()
        thumb = mthumb(self.source_album,
                       os.path.join(self.dest_album,constants.DIR_RESIZE),
                       constants.IMAGE_SIZES[self.resolution])
        while self.__attendi() and thumb.next():
            gtk.threads_enter()
            self.progressbar.set_fraction(self.count/self.total)
            gtk.threads_leave()
            self.count +=1

    def __build_html(self):
        # build html index
        self.__set_status_bar(label.MUM_PROGDIALOG_HTML)
        html_index = html_gallery(os.path.join(self.dest_album,constants.DIR_THUMB),
                                  constants.DIR_HTML,
                                  constants.MUM_THUMB_ROW,
                                  constants.MUM_THUMB_COL,
                                  os.path.join(label.MUM_THEME_LIST[self.theme],constants.MUM_THEME_INDEX),
                                  os.path.join(label.MUM_THEME_LIST[self.theme],constants.MUM_THEME_THUMBNAIL),
                                  self.title_album)
        html_index.build()
        # build html slide
        slide = html_slide(os.path.join(self.dest_album,constants.DIR_RESIZE),
                           os.path.join(self.dest_album,constants.DIR_HTML),
                           constants.DIR_THUMB,
                           os.path.join(label.MUM_THEME_LIST[self.theme],constants.MUM_THEME_IMAGE),
                           self.title_album)
        slide.build()


    def __upload_gallery(self):
        # upload gallery in website
        if not self.enable_web:
            return

        self.__set_status_bar(label.MUM_PROGDIALOG_WEB)
        upstr = update_ftp(self.WebUrl,
                           self.WebLogin,
                           self.WebPassword,
                           self.path_ftp)
        try:
            upstr.connect()
            try_connect = 0
        except socket.gaierror:
            self.__error(label.MUM_ERROR_HOST)
            return
            
        except no_dir_ftp:
            self.__error(label.MUM_ERROR_FTP_DIR)
            return
            
        except ftplib.error_perm:
            self.__error(label.MUM_ERROR_LOGIN)
            return
                
                
        finder = Finder(self.dest_album)

        try:
            if upstr.upstream(finder.get_dir(),finder.get_files()):
                try_upstr = 0
            else:
                self.__error(label.MUM_ERROR_SAME_DIR)
                return
            
        except no_dir_ftp:
            self.__error(label.MUM_ERROR_FTP_ROOT)
            return
            
        try:
            self.__set_status_bar(label.MUM_PROGDIALOG_SITE)
            while self.__attendi() and upstr.next():
                gtk.threads_enter()
                self.progressbar.set_fraction(self.count/self.total)
                gtk.threads_leave()
                self.count +=1
                # end upload
                
                        
        except socket.gaierror:
            self.__error(label.MUM_ERROR_UPSTR)
            return
            
    def __update_index(self):
        # Update index on website
        if not self.enable_update_index:
            return

        self.__set_status_bar(label.MUM_PROGDIALOG_INDEX)
        u = update_ftp_index(self.WebUrl,
                             self.WebLogin,
                             self.WebPassword,
                             os.path.join(label.MUM_THEME_LIST[self.theme],constants.MUM_THEME_INDEX),
                             self.path_ftp)
        gtk.threads_enter()
        self.progressbar.set_fraction(self.count/self.total)
        gtk.threads_leave()
        u.update(self.title_album,os.path.split(self.dest_album)[1])
