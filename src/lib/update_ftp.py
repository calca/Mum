""" Update ftp """

import ftplib
import os
import os.path

class no_dir_ftp:

    def __init__(self):
        pass

class update_ftp:
    
    def __init__(self,server=None,username=None,password=None,path=None):
        """
        Update ftp file in path

        @type server:string 
        @param server: ftp server
        @type username:string
        @param username: ftp login
        @type password:string
        @param password: ftp password
        @type path:string
        @param path: ftp path where put files
        """
        
        if server:
            self.set_server(server)

        if username:
            self.set_username(username)

        if password:
            self.set_password(password)

        self.set_path(path)
            
        # var 
        self.id = 0
        self.lock = 0
        self.verbose = 0
        self.is_connected = 0

    def set_server(self,server):
        self.server = server

    def set_username(self,username):
        self.user = username

    def set_password(self,password):
        self.password = password
        
    def set_path(self,path):
         if not len(path):
            path='.' # root sito
         self.path=path
            
    def __normalize_path(self,path,parent):
        path = path.replace(parent,'')
        path = path.replace('\\', '/')
        if path[-1] == '/':
            path = path[:-1]
        return path

    def __mkdir(self, ftp, dirs):
        for dir in dirs:
            dir=self.__normalize_path(dir,self.dir_parent)
            if self.verbose: print '-- mkd '+dir
            ftp.mkd(dir)

    def __is_dir_ftp(self,ftp,dir):

        try:
            ftp.cwd(dir)
            return 1
        except ftplib.error_perm:
            return 0

    def next(self):
        if not self.lock:

            if self.id >= len(self.files):
                self.ftp.quit()
                return 0
            
            up = self.files[self.id]
            up = self.__normalize_path(up,self.dir_parent)
            cmd = 'STOR ' + up
            if self.verbose: print cmd
            f = open(self.files[self.id], 'r')
            self.ftp.storbinary(cmd, f)
            
            self.id+=1
            return 1
        
        return 0

    def connect(self):
        self.ftp = ftplib.FTP(self.server)
        self.ftp.login(self.user, self.password)
        self.is_connected = 1

        try:
            self.ftp.cwd(self.path)
        except ftplib.error_perm:
            raise no_dir_ftp()

        return
    
    def upstream(self, dir, files):
        """
        @type dir:list
        @param dir: list of dir to update. Absolute path
        @type files:list
        @param files: list of files to update. Absolute path
        """
        self.files = files
        self.dir_parent, self.dir = os.path.split(dir[0])
        self.dir_parent += os.sep
        
        if len(files) == 0:
            self.lock = 1
            return -1 

        self.path=self.__normalize_path(self.path,self.dir_parent)

        if not self.is_connected:
            self.connect()
            
        if self.__is_dir_ftp(self.ftp,self.dir):
            if self.verbose: print '-- dir presente'
            self.ftp.quit()
            self.lock = 1
            return 0 # impossbile creare la dir web perche' gia esistente
        
        self.__mkdir(self.ftp,dir)
        return 1

    def upload(self):
        self.connect()
        while self.next():
            pass
        return 1
        

class Finder:
    
    def __init__(self,path):
        """ Find all files and directory in path

        @type path:string
        @param path: a full path
        """
        self.path=path
        self.file = []
        self.dir = []
        self.dir.append(path)
        self.find_all()
        return

    def _os_walk_callback(self, dummy, dir, names):
        if dir[-3:] == 'CVS':
            return
        for name in names:
            filename = os.path.join(dir, name)
            if name == 'CVS':
                continue
            elif name[-1] == '~':
                continue
            elif name[0] == '#':
                continue
            elif os.path.isdir(filename):
                self.dir.append(filename)
            else:
                self.file.append(filename)
        return

    def find_all(self):
        os.path.walk(self.path, self._os_walk_callback, None)
        return

    def get_files(self):
        return self.file
    
    def get_dir(self):
        return self.dir

if __name__ == '__main__':
    upstr = update_ftp('server','login','password','web_root')
    finder = Finder("/home/gigi/NewName")
    try:
        upstr.upstream(finder.get_dir(),finder.get_files())
        upstr.upload()
    except no_dir_ftp:
        print '--fanculo'
