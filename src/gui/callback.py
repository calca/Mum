''' Callback Function '''
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

from lib.utils import utility

import os
import label

class my_call:

    def __init__(self):
        pass

    
    def select_dir(self,parent,check,create_dir,default):
        self.path=''
        self.dlg = gtk.FileSelection(label.MUM_SELECT_DIR)
        self.parent=parent
        self.check=check
        
        if create_dir:
            self.dlg.show_fileop_buttons()
        else:
            self.dlg.hide_fileop_buttons()
             
        if not default == '' and os.path.isdir(default):
            self.dlg.set_filename(default+os.path.sep)
        else:
            self.dlg.set_filename(os.path.expanduser('~')+os.path.sep)

        self.dlg.ok_button.connect("clicked", self.return_ok)   
        # Connect the cancel_button to destroy the widget
        self.dlg.cancel_button.connect("clicked",
                                  lambda w: self.dlg.destroy())

        # don't select file
        self.dlg.file_list.set_sensitive(False)
        
        self.dlg.show()

    def return_ok(self,e):
        dir = self.dlg.get_filename()
        if self.check == "source":
            if self.__check_source(dir):
                self.parent.set_text(dir)
                self.dlg.destroy()
        if self.check == "dest":
            if self.__check_dest(dir):
                self.parent.set_text(dir)
                self.dlg.destroy()

        
    def __check_source(self,dir):
        if dir:
            if not utility().count_img(dir):
                self.empty_field(self.parent,label.MUM_ERROR_FOLDER_WHITOUT_IMAGES
                                 ,label.MUM_ERROR_FOLDER_WHITOUT_IMAGES_DES)
                return False
        return True

    def __check_dest(self,dir):
        if dir:
            if not utility().dir_is_empty(dir):
                self.empty_field(self.parent,label.MUM_ERROR_FOLDER_DEST_NOT_EMPTY
                                 ,label.MUM_ERROR_FOLDER_DEST_NOT_EMPTY_DES)
                return False
        return True
 
    def empty_field(self,parent,messaggio,spiegazione=""):
        dialog = gtk.MessageDialog(parent=None,
                                   flags=0,
                                   type=gtk.MESSAGE_WARNING,
                                   buttons=gtk.BUTTONS_NONE,
                                   message_format="<span weight=\"bold\" size=\"larger\">"+messaggio+"</span>\n\n"+spiegazione
                                   )
        
        dialog.set_title(label.MUM_TITLE_WINDOW)
        dialog.set_property("has-separator", False)       
        dialog.vbox.get_children()[0].get_children()[1].set_property("use-markup", True)
        
        dialog.add_button(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE)
            
        dialog.run()
        dialog.destroy()

    def stop_build(self,parent,messaggio,spiegazione=""):
        dialog = gtk.MessageDialog(parent,
                                   flags=0,
                                   type=gtk.MESSAGE_WARNING,
                                   buttons=gtk.BUTTONS_NONE,
                                   message_format="<span weight=\"bold\" size=\"larger\">"+messaggio+"</span>\n\n"+spiegazione
                                   )
        
        dialog.set_title(label.MUM_TITLE_WINDOW)
        dialog.set_property("has-separator", False)       
        dialog.vbox.get_children()[0].get_children()[1].set_property("use-markup", True)
        
        dialog.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        dialog.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
        res = dialog.run()
        if res == gtk.RESPONSE_OK:
            dialog.destroy()
            return True
        else:
            dialog.destroy()
            return False
        

