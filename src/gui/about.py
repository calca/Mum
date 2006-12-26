'''
Mum about dialog
'''
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

import label
import info

class About:
    def __init__(self,parent):
        
        self.dialog=gtk.Dialog(label.MUM_TITLE_WINDOW,
                               parent,
                               gtk.DIALOG_DESTROY_WITH_PARENT,
                               ( gtk.STOCK_CLOSE, gtk.RESPONSE_ACCEPT )
                               )
        
        logo = gtk.Image()
        logo.set_from_file(label.MUM_ICON)
        app_name = gtk.Label()
        app_name.set_markup("<span size='xx-large'><b>"+info.MUM_NAME+' '+info.MUM_VERSION+'</b></span>')
        copyright = gtk.Label()
        copyright.set_label(info.MUM_COPYRIGHT)
        copyright.set_selectable(True)
        author = gtk.Label()
        author.set_label(info.MUM_AUTHOR)
        author.set_selectable(True)
        description = gtk.Label()
        description.set_label(info.MUM_DESCRIPTION)
        description.set_justify(gtk.JUSTIFY_CENTER)
        description.set_selectable(True)
        
        self.dialog.set_resizable(False)
         
        self.dialog.vbox.pack_start(logo)
        self.dialog.vbox.pack_start(app_name)
        self.dialog.vbox.pack_end(copyright)
        self.dialog.vbox.pack_end(author)
        self.dialog.vbox.pack_end(description)
        self.dialog.vbox.set_spacing(8)
        self.dialog.vbox.set_border_width(4)
        self.dialog.vbox.show_all()
        

        self.dialog.set_has_separator(False)
        self.dialog.set_modal(False)
        self.dialog.run()
        self.dialog.destroy()




