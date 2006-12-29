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
        dialog = gtk.MessageDialog(parent,
                                   flags=0,
                                   type=gtk.MESSAGE_WARNING,
                                   buttons=gtk.BUTTONS_NONE,
                                   message_format="<span weight=\"bold\" size=\"larger\">"+messaggio+"</span>\n\n"+spiegazione
                                   )
        
        dialog.set_title(label.MUM_TITLE_WINDOW)
        dialog.set_property("use-markup", True)
        
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
        dialog.set_property("use-markup", True)
        
        dialog.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        dialog.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
        res = dialog.run()
        if res == gtk.RESPONSE_OK:
            dialog.destroy()
            return True
        else:
            dialog.destroy()
            return False
        

