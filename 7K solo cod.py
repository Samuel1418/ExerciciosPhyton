import gi
import null as null

gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class FiestraPrincpal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo saudo")
        caixa=Gtk.Box (spacing=6)
        self.btnSaudo= Gtk.Button (label="saudo") #creamos boton y su nombre
        self.btnSaudo.connect("clicked",self.on_btnsaudo_clicked) #Lo enlazamos con su funcion
        caixa.pack_end(self.btnSaudo, False,False, 6)#Boton ontroducido enla caja el pack_end o _start es para la posicion de lo que introduzcamos
        self.add(caixa) #añadimos caja al window que es el unico que deja que añadamos
        self.connect("destroy", Gtk.main_quit)

        self.txtNome = Gtk.Entry()
        self.txtNome.set_text("Escribe o teu nome") #Lo que va poner donde nos deja excribir
        caixa.pack_start(self.txtNome, True,True, 6) #Añadido a la caja

        self.lblsaudo= Gtk.Label()
        self.lblsaudo.set_text("Hola a todos") #Mensaje que va mostrar mientras no se le envie uno al pulsar el boton
        caixa.pack_start(self.lblsaudo, True, True, 6)  # Añadido a la caja


        self.show_all()

    def on_btnsaudo_clicked (self, btnSaludar):
            nome=self.txtNome.get_text()
            self.lblsaudo.set_text("Hola "+nome)




if __name__ == "__main__": #Seria el main de java, lamamos la calse Fiestra principal y luego llamamos el main del gtk
        FiestraPrincpal()
        Gtk.main()