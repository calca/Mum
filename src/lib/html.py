""" Class for build html from tag """

class html:

    def __init__(self,pag_template=None,pag_dest=None,list=None):
        """
        Constructor for html class

        @type pag_template: string
        @param pag_template: uri for file template
        @type pag_dest: string
        @param pag_dest: uri for file created html file
        @type list:dictionary
        @param list: dictionary tag whit replace string
        """
        if pag_template:
            self.set_template(pag_template)

        if pag_dest:
            self.set_destination(pag_dest)

        if list:
            self.set_list_tag(list)


    def set_template(self,name):
        """
        Imposta il file template
        @type name: string
        @param name: uri for file template
        """
        if os.path.isfile(pag_template):
            self.pag_template
            self.pt_ok=1
            return 1
        else:
            print "html:: pag_template isn't a file"
            return 0

    def set_destination(self,name):
        """
        Imposta il file di destinazione
        @type name: string
        @param name: uri for file template
        """
        self.pag_dest=name
        self.pd_ok=1
        return

    def set_list_tag(self,list):
        """
        Imposta il dictionary
        @type list:dictionary
        @param list: dictionary tag whit replace string
        """
        self.list=list
        self.li_ok=1

    def load_page(self,page):
        f_pagina = file(page, "r")
        pagina = f_pagina.read()
        f_pagina.close()
        return pagina
    
    def build_html(self,pagina,list):
        for k, v in list.items():
            pagina=pagina.replace(k,v)
        return pagina

    def write_page(self,pagina,name):
        f_pagina = file(name, "w")
        f_pagina.write(pagina)
        f_pagina.close()

    def save(self):
        self.write_page(self.build_html
                        (self.load_page
                         (self.pag_template),
                         self.list),
                        self.pag_dest)
    
