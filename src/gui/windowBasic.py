"""
Mum main window
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
##  *  Copyright 2004 Calcaterra Gianluigi <gianluigi.calcaterra@gmail.com>
##  *
##  */



import gtk
import gobject

import re,time

from callback import *
from about import About
import label
from lib import constants
from lib.utils import utility
from preview import show_preview
from mum_build import mum_build

class windowBasic:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
 
        self.ClassTitolo = gtk.Image()
        self.ClassTitolo.set_from_file(label.MUM_TITLE_IMAGE)
        self.ClassTitolo.set_size_request(450,-1)
        self.ClassTitolo.set_alignment(0,0)
        self.AlbumsLabel = gtk.Label("<span size='large'><b>"+label.MUM_ALBUM+'</b></span>')
        self.AlbumsLabel.set_use_markup(True)
        self.TitleLabel = gtk.Label(label.MUM_TITLE_GALLERY)
        self.TitleAlbum = gtk.Entry(60)
        self.FolderLabel = gtk.Label(label.MUM_FOLDER_IMAGES)
	# Browser Button
	self.BrowserButtonSource=gtk.FileChooserButton('Select a Folder Source') 
	self.BrowserButtonSource.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
	self.BrowserButtonSource.set_current_folder(os.path.expanduser('~')+os.path.sep)
        self.FolderGalleryLabel = gtk.Label(label.MUM_FOLDER_GALLERY)
	self.BrowserButtonDest=gtk.FileChooserButton('Select a Folder Destination')
	self.BrowserButtonDest.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
	self.BrowserButtonDest.set_current_folder(os.path.expanduser('~')+os.path.sep)
        self.checkboxWeb = gtk.CheckButton(label.MUM_UPLOAD)
        self.LabelFtpAdress = gtk.Label(label.MUM_FTP_ADDRESS)
        self.WebUrl =gtk.Entry()
        self.LabelUsername = gtk.Label(label.MUM_FTP_USERNAME)
        self.WebLogin = gtk.Entry()
        self.PasswordLabel = gtk.Label(label.MUM_FTP_PASSWORD)
        self.WebPassword = gtk.Entry()
        self.WebPassword.set_visibility(False)
        self.RootLabel = gtk.Label(label.MUM_WEB_ROOT)
        self.RootDir = gtk.Entry()
        self.CheckUpdateIndex = gtk.CheckButton(label.MUM_UPDATE_INDEX)
        self.Closebutton = gtk.Button(stock=gtk.STOCK_CLOSE)
        self.Nextbutton = gtk.Button(label.MUM_PUBBLIC,gtk.STOCK_EXECUTE)
        self.Aboutbutton = gtk.Button(label.MUM_ABOUT,gtk.STOCK_HELP)
        # Option menu Resolution
        self.ResolutionLabel = gtk.Label(label.MUM_RESOLUTION)
        self.ResolutionMenu = gtk.combo_box_new_text()
        for i in label.MUM_LABEL_RES:
            self.ResolutionMenu.append_text(i)
        self.ResolutionMenu.set_active(0)
        self.PreviewButton = gtk.Button(label.MUM_PREVIEW)
        self.PreviewLabel = gtk.Label(label.MUM_ALBUM_THEME)
        # Option Menu Theme
        self.PreviewMenu = gtk.combo_box_new_text()
        self.ListaThemes = label.MUM_THEME_LIST.keys() 
        self.ListaThemes.reverse()
        for i in self.ListaThemes:
            self.PreviewMenu.append_text(i)
        self.PreviewMenu.set_active(0)

        # progressbar
        self.progressbar= gtk.ProgressBar()
        # stastusbar
        self.statusbar = gtk.Statusbar()
        self.statusbar.set_has_resize_grip(False)
        
        # disable feature
        self.__disable_web()
        
        self.__set_properties()
        self.__do_layout()

        # upload only ?
        self.__upload_only=False
        self.__handle_error=True
        
        self.__init_thread()
        
        # event
        self.Nextbutton.connect("clicked",self.next)
        self.Closebutton.connect("clicked",self.button_close)
        self.Aboutbutton.connect("clicked",self.button_about)
        self.PreviewButton.connect("clicked",self.button_preview)
        self.checkboxWeb.connect("toggled",self.web)
        self.statusbar.connect("text-popped",self.end_mum_build)

        self.TitleAlbum.connect("key-press-event",self.reset_progressbar)

     
    def __init_thread(self):
        
        # push message in status bar
        id_status  = self.statusbar.get_context_id("1")
        self.statusbar.push(id_status,"")
        # prepare progressbar
        self.th_mum_build=mum_build(self.window,self.progressbar,self.statusbar,id_status)
        self.__new_thread=False
            
    def __set_properties(self):
        self.window.set_title(label.MUM_TITLE_WINDOW)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_resizable(False)
        icon = gtk.gdk.pixbuf_new_from_file(label.MUM_ICON)
        self.window.set_icon_list(icon)



    def __pack_label_hig(self,widget):

        spazio = gtk.Label("    ")
        box= gtk.HBox()
        box.pack_start(spazio,False,False,0)
        box.pack_start(widget,False,False,0)

        return box

    def __do_layout(self):
        layout_page = gtk.VBox()
        
        grid_gal = gtk.Table(13, 3)

        #Align widget
        self.AlbumsLabel.set_alignment(0,0)

        #layout
        layout_page = gtk.VBox()
        grid_gal = gtk.Table(13, 3)

        layout_page.pack_start(self.ClassTitolo)
        grid_gal.attach(self.AlbumsLabel, 0, 1, 0, 1, gtk.FILL, gtk.FILL, 8, 8)
        grid_gal.attach(self.__pack_label_hig(self.TitleLabel), 0, 1, 1, 2)
        grid_gal.attach(self.TitleAlbum, 1, 2, 1, 2 )
        grid_gal.attach(self.__pack_label_hig(self.FolderLabel), 0, 1, 2, 3)
        grid_gal.attach(self.BrowserButtonSource, 1, 2, 2, 3 )
        grid_gal.attach(self.__pack_label_hig(self.FolderGalleryLabel), 0, 1, 3, 4 )
        grid_gal.attach(self.BrowserButtonDest, 1, 2, 3, 4)
        grid_gal.attach(self.__pack_label_hig(self.ResolutionLabel), 0, 1, 4, 5)
        grid_gal.attach(self.ResolutionMenu, 1, 2, 4, 5)
        grid_gal.attach(self.__pack_label_hig(self.PreviewLabel), 0, 1, 5, 6)
        grid_gal.attach(self.PreviewMenu, 1, 2, 5, 6)
        grid_gal.attach(self.PreviewButton, 2, 3, 5, 6)
        grid_gal.attach(self.__pack_label_hig(self.checkboxWeb), 0, 3, 7, 8)    
        grid_gal.attach(self.__pack_label_hig(self.LabelFtpAdress), 0, 1, 8, 9)
        grid_gal.attach(self.WebUrl, 1, 2, 8, 9)
        grid_gal.attach(self.__pack_label_hig(self.LabelUsername),  0, 1, 9, 10)
        grid_gal.attach(self.WebLogin,  1, 2, 9, 10)
        grid_gal.attach(self.__pack_label_hig(self.PasswordLabel), 0, 1, 10, 11)
        grid_gal.attach(self.WebPassword,  1, 2, 10, 11)
        grid_gal.attach(self.__pack_label_hig(self.RootLabel), 0, 1, 11, 12)
        grid_gal.attach(self.RootDir,  1, 2, 11, 12)
        grid_gal.attach(self.__pack_label_hig(self.CheckUpdateIndex), 0, 3, 12, 13)

        grid_gal.set_row_spacings(6)
        grid_gal.set_col_spacings(6)
        
        layout_page.pack_start(grid_gal)

        bar_about=gtk.HButtonBox()
        bar_about.set_layout(gtk.BUTTONBOX_START)
        bar_about.pack_start(self.Aboutbutton)

        bar_action=gtk.HButtonBox()
        bar_action.set_layout(gtk.BUTTONBOX_END)
        bar_action.set_spacing(6)
        bar_action.pack_end(self.Closebutton)
        bar_action.pack_end(self.Nextbutton)

        bar = gtk.HBox(True)
        bar.pack_start(bar_about)
        bar.pack_end(bar_action)

        grid_gal.set_border_width(6)
        bar.set_border_width(6)

        layout_page.pack_start(bar)

        stat = gtk.HBox(False)
        stat.pack_start(self.progressbar,False,True)
        stat.pack_end(self.statusbar,True,True)
        
        layout_page.pack_start(stat)
        
        self.window.add(layout_page)
        
            
    def web(self,e):
        
        if self.checkboxWeb.get_active():
            self.__active_web()
        else:
            # disable feature
            self.__disable_web()

    def __active_web(self):
        self.LabelFtpAdress.set_sensitive(True)
        self.LabelUsername.set_sensitive(True)
        self.PasswordLabel.set_sensitive(True)
        self.WebUrl.set_sensitive(True)
        self.WebLogin.set_sensitive(True)
        self.WebPassword.set_sensitive(True)
        self.RootLabel.set_sensitive(True)
        self.RootDir.set_sensitive(True)
        self.CheckUpdateIndex.set_sensitive(True)

    def __disable_web(self):
        self.LabelFtpAdress.set_sensitive(False)
        self.LabelUsername.set_sensitive(False)
        self.PasswordLabel.set_sensitive(False)
        self.WebUrl.set_sensitive(False)
        self.WebLogin.set_sensitive(False)
        self.WebPassword.set_sensitive(False)
        self.RootLabel.set_sensitive(False)
        self.RootDir.set_sensitive(False)
        self.CheckUpdateIndex.set_sensitive(False)

    def __active_mum(self):
        self.TitleLabel.set_sensitive(True)
        self.TitleAlbum.set_sensitive(True)
        self.FolderLabel.set_sensitive(True)
        self.BrowserButtonSource.set_sensitive(True)
        self.ResolutionLabel.set_sensitive(True)
        self.ResolutionMenu.set_sensitive(True)
        self.PreviewButton.set_sensitive(True)
        self.PreviewLabel.set_sensitive(True)
        self.PreviewMenu.set_sensitive(True)
        self.FolderGalleryLabel.set_sensitive(True)
        self.BrowserButtonDest.set_sensitive(True)
        self.checkboxWeb.set_sensitive(True)
        self.Closebutton.set_sensitive(True)
        self.Nextbutton.set_label(gtk.STOCK_EXECUTE)
        self.Aboutbutton.set_sensitive(True)
        if self.checkboxWeb.get_active():
            self.__active_web()

    def __disable_mum(self):
        self.TitleLabel.set_sensitive(False)
        self.TitleAlbum.set_sensitive(False)
        self.FolderLabel.set_sensitive(False)
        self.BrowserButtonSource.set_sensitive(False)
        self.FolderGalleryLabel.set_sensitive(False)
        self.BrowserButtonDest.set_sensitive(False)
        self.ResolutionLabel.set_sensitive(False)
        self.ResolutionMenu.set_sensitive(False)
        self.PreviewButton.set_sensitive(False)
        self.PreviewLabel.set_sensitive(False)
        self.PreviewMenu.set_sensitive(False)
        self.checkboxWeb.set_sensitive(False)
        self.Closebutton.set_sensitive(False)
        self.Aboutbutton.set_sensitive(False)
        self.__disable_web()

    def next(self,e):

        if self.th_mum_build.isAlive():
            self.__stop_mum_build()
        else:
            self.reset_status_bar()
            self.__execute()


    def __stop_mum_build(self):
        self.th_mum_build.suspende_thread()
        d = my_call()
        res = d.stop_build(self.window,label.MUM_STOP_BUILD,label.MUM_STOP_BUILD_DES)
        if res :
            self.th_mum_build.terminate()
            self.window.window.set_cursor(None)
            self.__active_mum()
            return True
        else:
            self.th_mum_build.resume_thread()   
            return False
    
    def __execute(self):
        """ Launch thread and performe operation """
        if self.TitleAlbum.get_text() == '':
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_TITLE,label.MUM_ERROR_TITLE_DES)
            self.TitleAlbum.grab_focus()
            return
        
        if not utility().count_img(self.BrowserButtonSource.get_current_folder()):
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_FOLDER_WHITOUT_IMAGES,
                          label.MUM_ERROR_FOLDER_WHITOUT_IMAGES_DES)
            self.BrowserButtonSource.grab_focus()
            return
        
        if not os.path.isdir(self.BrowserButtonSource.get_current_folder()):
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_FOLDER_IMAGE,label.MUM_ERROR_FOLDER_IMAGE_DES)
            return
        
        if not os.path.isdir(self.BrowserButtonDest.get_current_folder()):
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_FOLDER_DEST,label.MUM_ERROR_FOLDER_DEST_DES)
            self.BrowserButtonDest.grab_focus()
            return

        if not utility().dir_is_empty(self.BrowserButtonDest.get_current_folder()) and not self.__upload_only:
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_FOLDER_DEST_NOT_EMPTY,
                          label.MUM_ERROR_FOLDER_DEST_NOT_EMPTY_DES)
            self.BrowserButtonDest.grab_focus()
            return
        
        if self.BrowserButtonDest.get_current_folder() == self.BrowserButtonSource.get_current_folder():
            d = my_call()
            d.empty_field(self.window,label.MUM_ERROR_FOLDER,label.MUM_ERROR_FOLDER_DES)
            self.BrowserButtonDest.grab_focus()
            return

        # show dir have space.
        if os.path.isdir(self.BrowserButtonDest.get_current_folder()):
            a, dir =os.path.split(self.BrowserButtonDest.get_current_folder())
            if  dir.count(' '):
                d = my_call()
                d.empty_field(self.window,label.MUM_ERROR_SPACE_IN_FOLDER
                              ,label.MUM_ERROR_SPACE_IN_FOLDER_DES)
                self.BrowserButtonDest.grab_focus()
                return
            
        if self.checkboxWeb.get_active():    
            if self.WebUrl.get_text() == '':
                d = my_call()
                d.empty_field(self.window,label.MUM_ERROR_FTP_ADDRESS
                              ,label.MUM_ERROR_FTP_ADDRESS_DES)
                self.WebUrl.grab_focus()
                return

            if self.WebLogin.get_text() == '':
                d = my_call()
                d.empty_field(self.window,label.MUM_ERROR_FTP_LOGIN
                              ,label.MUM_ERROR_FTP_LOGIN_DES)
                self.WebLogin.grab_focus()
                return
            
            if self.WebPassword.get_text() == '':
                d = my_call()
                d.empty_field(self.window,label.MUM_ERROR_FTP_PASSWORD
                              ,label.MUM_ERROR_FTP_PASSWORD_DES)
                self.WebPassword.grab_focus()
                return

        # re init_thread
        self.__init_thread()
       
        self.th_mum_build.set_theme(self.ListaThemes[self.PreviewMenu.get_active()])
        self.th_mum_build.set_resolution(self.ResolutionMenu.get_active())
        self.th_mum_build.set_title_album(self.TitleAlbum.get_text())
        self.th_mum_build.set_source_album(self.BrowserButtonSource.get_current_folder())
        self.th_mum_build.set_dest_album(self.BrowserButtonDest.get_current_folder())
        if  self.checkboxWeb.get_active():
            self.th_mum_build.set_enable_web()
            self.th_mum_build.set_web_url(self.WebUrl.get_text())
            self.th_mum_build.set_web_login(self.WebLogin.get_text())
            self.th_mum_build.set_web_password(self.WebPassword.get_text())
            self.th_mum_build.set_web_rootdir(self.RootDir.get_text())
            if self.CheckUpdateIndex.get_active():
                self.th_mum_build.set_enable_update_index()

        # enalbe upload only
        if self.__upload_only:
            self.th_mum_build.set_enable_upload_only()

        self.Nextbutton.set_label(gtk.STOCK_CANCEL)
        self.__disable_mum()
        # busy cursor
        watch = gtk.gdk.Cursor (gtk.gdk.WATCH)
        self.window.window.set_cursor(watch)
        # Ristabilisce il controllo errori
        self.__handle_error=True
        # run thread
        self.th_mum_build.start()
             
                
    def end_mum_build(self,e,a,b):

        if not self.__handle_error:
            return

        # handle error
        if self.th_mum_build.have_error():
            self.__handle_error = False
            self.__upload_only = True
            self.__active_mum()
            
            if self.th_mum_build.get_error() == label.MUM_ERROR_HOST:
                self.Nextbutton.set_label(gtk.STOCK_GO_FORWARD)
                self.WebUrl.grab_focus()

            if self.th_mum_build.get_error() == label.MUM_ERROR_FTP_DIR:
                self.Nextbutton.set_label(gtk.STOCK_GO_FORWARD)
                self.RootDir.grab_focus()

            if self.th_mum_build.get_error() == label.MUM_ERROR_LOGIN:
                self.Nextbutton.set_label(gtk.STOCK_GO_FORWARD)
                self.WebLogin.grab_focus()

            if self.th_mum_build.get_error() == label.MUM_ERROR_SAME_DIR:
                self.Nextbutton.set_label(gtk.STOCK_GO_FORWARD)
            

            self.window.window.set_cursor(None)

            return

        # deve essere finito!
        if not a == 2 :
            return
        
        # correct end
        self.__new_thread = True
        self.__upload_only = False
        
        self.TitleAlbum.set_text("")
	self.BrowserButtonSource.set_current_folder(os.path.expanduser('~')+os.path.sep)
	self.BrowserButtonDest.set_current_folder(os.path.expanduser('~')+os.path.sep)

        self.window.window.set_cursor(None)

        self.__active_mum()

    def reset_status_bar(self):
        # hardcoded id utilizzato nel thread
        self.statusbar.pop(2)
        
    def reset_progressbar(self,e,b):
        if self.progressbar.get_fraction() > 0:
            self.progressbar.set_fraction(0)
            self.reset_status_bar()

    def button_close(self,e):
        gtk.main_quit()

    def button_about(self,e):
        About(self.window)
        
    def delete_event(self, widget, event, data=None):
        
        if self.th_mum_build.isAlive():
            self.__stop_mum_build()
            return True
            
        # close application
        gtk.main_quit()
      
    def __select_theme(self,e,data):
        self.__theme=data
        if self.__theme_have_preview(self.__theme): 
            self.PreviewButton.set_sensitive(True)
        else:
            self.PreviewButton.set_sensitive(False)

    def __theme_have_preview(self,name):
        """ Controlla la presenza dell'immagine di
        anteprima"""
        if name in label.MUM_THEME_LIST.keys():
            img=os.path.join(label.MUM_THEME_LIST[self.__theme],constants.MUM_THEME_PREVIEW)
            if os.path.isfile(img):
                return True
            else:
                return False
        else:
                return False

    def __select_resolution(self,e,data):
        self.__resolution=label.MUM_LABEL_RES.index(data)
        

    def button_preview(self,e):
        img=os.path.join(label.MUM_THEME_LIST[self.ListaThemes[self.PreviewMenu.get_active()]],constants.MUM_THEME_PREVIEW)
        dlg=show_preview(self.window,img)
        
    
    def main(self):
        gtk.gdk.threads_init()
        
        self.window.connect("delete_event", self.delete_event)
        self.window.show_all()

        gtk.gdk.threads_enter()
        gtk.main()
        gtk.gdk.threads_leave()




