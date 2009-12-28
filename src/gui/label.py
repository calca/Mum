''' String in the UI '''
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


import os,sys
from lib.utils import utility

mum_path = os.path.abspath(os.path.dirname(sys.argv[0]))

MUM_TITLE_WINDOW='mum'
MUM_ALBUM='Album'
MUM_TITLE_GALLERY='Title gallery:'
MUM_FOLDER_IMAGES='Folder images:'
MUM_BROWSER='Browser ...'
MUM_FOLDER_GALLERY='Folder gallery:'
MUM_FTP_ADDRESS='FTP host:'
MUM_FTP_PASSWORD='Password:'
MUM_FTP_USERNAME='Username:'
MUM_ABOUT='About'
MUM_RESOLUTION='Resolution:'
MUM_ALBUM_THEME='Album theme:'
MUM_PUBBLIC='Create ...'
MUM_UPDATE_INDEX='Update index.html'
MUM_WEB_ROOT="FTP path:"
MUM_UPLOAD="Upload on website"
MUM_PREVIEW="Preview ..."
MUM_SELECT_DIR="Select Folder"
MUM_COMPLETED_OPERATION="Operation completed"
MUM_STOP_OPERATION="Operation stoped"

MUM_ICON_WIN=utility().fix_path(os.path.join(mum_path,'data','mum.ico'))
MUM_ICON=utility().fix_path(os.path.join(mum_path,'data','mum.png'))

MUM_LABEL_RES=["Low Quality", "Medium Quality", "High Quality"]
MUM_TOOLTIP_RES=["Resize at 640x480", "Resize at 800x600", "Resize at 1024x768"]

MUM_TITLE_IMAGE=utility().fix_path(os.path.join(mum_path,'data','mum.jpg'))

MUM_THEME_LIST=utility().themes(utility().fix_path(os.path.join(mum_path,'template')))

# Error
MUM_ERROR_TITLE="Title gallery is empty"
MUM_ERROR_FOLDER_IMAGE="Invalid Folder images"
MUM_ERROR_FOLDER_DEST="Invalid Folder gallery"
MUM_ERROR_FTP_ADDRESS="FTP host is empty"
MUM_ERROR_FTP_LOGIN="Username is empty"
MUM_ERROR_FTP_PASSWORD="Password is empty"
MUM_ERROR_FOLDER_WHITOUT_IMAGES="Folder haven't Images"
MUM_ERROR_FOLDER="Folder image and Folder gallery are same!!!"
MUM_ERROR_SPACE_IN_FOLDER="Folder gallery have space character"
MUM_ERROR_FOLDER_DEST_NOT_EMPTY="Folder gallery isn't empty"
MUM_ERROR_SPACE_ROOT="FTP path have space character"

# Error Description
MUM_ERROR_TITLE_DES="Album need a title that is display in web pages"
MUM_ERROR_FOLDER_IMAGE_DES="Folder don't have any images or isn't valid path"
MUM_ERROR_FOLDER_DEST_DES="Folder isn't empty or isn't valid path"
MUM_ERROR_FTP_ADDRESS_DES="Specify host to connect for upload gallery"
MUM_ERROR_FTP_LOGIN_DES="Specify username to login to host"
MUM_ERROR_FTP_PASSWORD_DES="Specify password to login to host"
MUM_ERROR_FOLDER_WHITOUT_IMAGES_DES=""
MUM_ERROR_FOLDER_DES="Folder image and Folder gallery could different because only album is put on web site"
MUM_ERROR_SPACE_IN_FOLDER_DES="URL not permit a space character"
MUM_ERROR_FOLDER_DEST_NOT_EMPTY_DES="Put the gallery in an empty folder"
MUM_ERROR_SPACE_ROOT="URL not permit a space character"

# Progress Dialog
MUM_PROGDIALOG_STOP="La creazione dell'album e' stata interrotta"
MUM_PROGDIALOG_THUMB="Creating thumbnail ..."
MUM_PROGDIALOG_IMAGE="Resize image ..."
MUM_PROGDIALOG_HTML="Creating html ..."
MUM_PROGDIALOG_WEB="Connecting at website ..."
MUM_PROGDIALOG_INDEX="Updating index ..."
MUM_PROGDIALOG_SITE="Upload gallery ..."

# Error
MUM_ERROR_HOST="Host don't respond"
MUM_ERROR_FTP_DIR="FTP path is wrong"
MUM_ERROR_LOGIN="Username or password are wrong"
MUM_ERROR_SAME_DIR="Folder gallery is just present in ftp"
MUM_ERROR_FTP_ROOT="FTP root is wrong"
MUM_ERROR_UPSTR="Connection down"

# Stop Dialog
MUM_STOP_BUILD="Stop creation album?"
MUM_STOP_BUILD_DES="Remove album from computer and clean ftp"
