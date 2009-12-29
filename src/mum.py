#!/usr/bin/python

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


''' Main File '''


__version__ = '1.3.1'
__author__ = 'Gianluigi Calcaterra <gianluigi.calcaterra@gmail.com>'

import os, sys

from gui import mum

def main():      
    mum_path = os.path.abspath(os.path.dirname(sys.argv[0]))
    sys.path = [mum_path] + sys.path
    g = mum.mum_app()
    g.main()
    
if __name__ == "__main__":
    main()
