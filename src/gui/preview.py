"""
Window that show preview
"""
## /*
##  *              ,           , 
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

import label

class show_preview:
    
    def __init__(self,parent,image):

        self.dialog=gtk.Dialog(label.MUM_TITLE_WINDOW,
                               parent,
                               gtk.DIALOG_DESTROY_WITH_PARENT,
                               ( gtk.STOCK_CLOSE, gtk.RESPONSE_ACCEPT )
                               )
        bitmap = gtk.Image()
        bitmap.set_from_file(image)
        self.dialog.vbox.pack_start(bitmap)
        bitmap.show()
        self.dialog.set_has_separator(False)
        self.dialog.set_modal(False)
        self.dialog.run()
        self.dialog.destroy()







