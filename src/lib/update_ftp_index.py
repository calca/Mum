""" update index.html in root ftp """

import ftplib,os,tempfile

import html, constants

class update_ftp_index(html.html):
    
    def __init__(self,server,username,password,tpl_page,path):
        """
        Update index page

        @type server:string
        @param server: ftp server
        @type username:string
        @param username: ftp login
        @type password: string
        @param password: ftp password
        @type tpl_page: string
        @param tpl_page: page template for index
        @type path:string
        @type path: where puth and get index file in ftp server
        """
        
        if not os.path.isfile(tpl_page):
            print 'update_ftp_html:: file tpl_page not found'
        self.server = server
        self.user = username
        self.password = password
        self.tpl_page = tpl_page
        self.path=path
        self.dwl_page = ''
        return

    def __connect(self):
        self.ftp = ftplib.FTP(self.server)
        self.ftp.login(self.user, self.password)


    def txtwriter(self,line):
        self.dwl_page+=line+"\n"

    def __update_index(self,titolo,link):
        #name=tempfile.mktemp()
        name=os.tempnam()

        d = {}
        try:
            self.ftp.retrlines("RETR "+self.path+'/index.html',self.txtwriter)
            pagina = self.dwl_page
        except ftplib.error_perm:
            pagina=self.load_page(self.tpl_page)
            d[constants.MUM_INDEX_TITLE]=' Gallery Index '
            d[constants.MUM_INDEX_TABLE]=constants.MUM_INDEX_WEB_TAG
            d[constants.MUM_INDEX_MENU]=''
            
        d[constants.MUM_INDEX_WEB_TAG]='<li><a href=%s>%s</a></li>\n%s\n%s' % ( link, titolo, constants.MUM_INDEX_WEB_TAG, constants.MUM_INDEX_WEB_INFO )
        pagina = self.build_html(pagina,d)
        self.write_page(pagina,name)
        cmd = 'STOR ' + self.path+'/index.html'
        f = open(name, 'r')
        self.ftp.storbinary(cmd, f)
        
    def update(self,titolo,link):
        self.__connect()
        self.__update_index(titolo,link)
        self.ftp.close()



if __name__ == '__main__':

     u = update_ftp_index('server','login','pwd','template_index','dest_folder')
     u.update('questo e titolo','questo il link')
