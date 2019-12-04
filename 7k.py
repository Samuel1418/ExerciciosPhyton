import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class FiestraPrincpal():
    def __init__(self):
        builder=Gtk.Builder()
        builder.add_from_file("7k")

        fPrincipal = builder.get_object("fiestraPrincipal") #Nombre del gtk window
        self.txtNome=builder.get_object("saudo") #Nombre gtk entry
        self.lblsaudo=builder.get_object("label") #Nombre label
        self.btnsaudo=builder.get_object("btnSaludar") #nombre del boton


        sinais={
            "on_btnsaudo_clicked": self.on_btnsaudo_clicked,
            "on_nome_activate": self.on_nome_activate,
            "on_Prueba_destroy": Gtk.main_quit  #metodo que ya viene con el gtk el destry se hace en la ventana raiz
        }

        builder.connect_signals(sinais)
        fPrincipal.show_all()


    def on_btnsaudo_clicked (self, btnSaludar):
            nome=self.txtNome.get_text()
            self.lblsaudo.set_text("Hola "+nome)

    def on_nome_activate(self, cadrotexto):
            self.on_btnsaudo_clicked(cadrotexto)

if __name__ == "__main__":
        FiestraPrincpal()
        Gtk.main()