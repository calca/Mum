""" Common utils """

import re, os, shutil

import constants

class utility:

    def list_img(self,path_img):
        
        if not os.path.isdir(path_img):
            print "(utility::list_img) invalid path_img"
            return False

        rs = r'\.('
        for extension in constants.IMAGE_TYPES:
            rs += extension + '|'
            image_regexp = re.compile(rs[:-1] + ')$', re.I)
            
        valid_files = filter(image_regexp.search, os.listdir(path_img))
        return valid_files

    def count_img(self,path_img):

        if not os.path.isdir(path_img):
            return False
        
        return len(self.list_img(path_img))          
        
    def copy_img(self,path_source,path_dest):

        if not os.path.isdir(path_source):
            print "(utility::copy_img) invalid path_source"
            return False

        if not os.path.isdir(path_dest):
            print "(utility::copy_img) invalid path_dest"
            return False

        for x in self.list_img(path_source):
            if not ( x == 'example.png' ): #hardcoded
                shutil.copy(os.path.join(path_source,x),path_dest)

    def fix_path(self,path):
        """\
        Returns an absolute version of path, accroding to the invoking dir of
        wxglade (which can be different from '.' if it is invoked from a shell
        script)
        """
        if not os.path.isabs(path):
            return os.path.join(os.getcwd(), path)
        return path

    def is_theme(self,dir):
        '''
        Controlla che la directory
        contenga i file per il thema

        @type dir:string
        @param dir:path theme
        '''
        if os.path.isdir(dir):
            if os.path.isfile(os.path.join(dir,constants.MUM_THEME_INDEX)):
                              if os.path.isfile(os.path.join(dir,constants.MUM_THEME_IMAGE)):
                                                if os.path.isfile(os.path.join(dir,constants.MUM_THEME_THUMBNAIL)):
                                                                  return 1
        return 0
                                                                 
    def themes(self,dir):
        '''
        Return a list of themes installed
        
        @type dir: string
        @param dir: path where are stored themes
        '''
        lista = {}
        for theme in os.listdir(dir):
            full_theme=os.path.join(dir,theme)
            if self.is_theme(full_theme):
                lista[theme] = full_theme

        return lista
                

    def dir_is_empty(self,dir):
        files = os.listdir(dir)
        if not len(files):
            return 1
        return 0
