import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Fiestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk")

        caixa= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(caixa)

        stack=Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        casinhaVerificacion= Gtk.CheckButton("Púlsame")
        stack.add_titled(casinhaVerificacion,"Check","Casiña verificación") #lo que añadimos, nombre y titulo

        etiqueta= Gtk.Label()
        etiqueta.set_markup("<big>Unha etiqueta simple</big>")
        stack.add_titled(etiqueta,"Etiqueta","Unha etiqueta")

        panel= Panel()
        stack.add_titled(panel,"panel","Panel con botons")

        stack_switcher= Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)#el stack ya tiene el resto dentro

        caixa.pack_start(stack_switcher, True,True,0)
        caixa.pack_start(stack, True,True,0)



        self.connect("destroy", Gtk.main_quit)

        self.show_all()

class Panel(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)

        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")
        boton7 = Gtk.Button(label="Boton 7")
        boton8 = Gtk.Button(label="Boton 8")
        boton9 = Gtk.Button(label="Boton 9")

        self.add(boton1)
        self.attach(boton2, 1, 0, 2, 1)
        self.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        #grid.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        #grid.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        #comentamos el boton 5 y 6 para poner en su sitio esta caja con tres botones
        caixa= Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        caixa.pack_start(boton7, True,True, 0)
        caixa.pack_start(boton8, True, True, 0)
        caixa.pack_start(boton9, True, True, 0)
        self.attach_next_to(caixa,boton4, Gtk.PositionType.BOTTOM,1,2)



if __name__ == "__main__":
    Fiestra()
    Gtk.main()