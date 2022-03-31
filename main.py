from kivy.lang import Builder
from kivymd.app import MDApp

from model import Model

#from donaclotilde.model import Model
#from guia import principal, menu , pesquisa, pesquisa_botao


asd=Model()
asd.listall()
class GuiaApp(MDApp):
    def __init__(self, *args):
        super(GuiaApp, self).__init__(*args)
        self.asd=Model()
        #self.asd.banco=GuiaApp.get_running_app().user_data_dir+"/database.db"
        self.filtro = ''

    def listar(self):
        print('asdd')

GuiaApp().run()
