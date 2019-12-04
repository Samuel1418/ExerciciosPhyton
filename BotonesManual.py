import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk.Grid")

        grid = Gtk.Grid()
        self.add(grid)

        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")
        boton7 = Gtk.Button(label="Boton 7")
        boton8 = Gtk.Button(label="Boton 8")
        boton9 = Gtk.Button(label="Boton 9")

        grid.add(boton1)
        grid.attach(boton2, 1, 0, 2, 1)
        grid.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        #grid.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        #grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        #comentamos el boton 5 y 6 para poner en su sitio esta caja con tres botones
        caixa= Gtk.Box()
        caixa.pack_start(boton7, True,True, 0)
        caixa.pack_start(boton8, True, True, 0)
        caixa.pack_start(boton9, True, True, 0)
        grid.attach_next_to(caixa,boton4, Gtk.PositionType.BOTTOM,1,1)



        self.connect("destroy", Gtk.main_quit)

        self.show_all()
if __name__ == "__main__":
    Fiestra()
    Gtk.main()