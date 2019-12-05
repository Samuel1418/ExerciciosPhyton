# importamos la libreria
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WPrincipal1(Gtk.Window):

    def __init__(self):
        # al heredar de window heradmos su constructor
        Gtk.Window.__init__(self, title="Ejemplo TreeView")
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        # Modelo
        modelo = Gtk.ListStore(str, str, float, bool, int)
        modelo.append(["Hotel 1", "Calle 1", 70.0, True, 1])
        modelo.append(["Hotel 2", "Calle 2", 70.0, False, 2])
        modelo.append(["Hotel 3", "Calle 3", 70.0, True, 5])

        # Vista
        vista = Gtk.TreeView(model=modelo)

        # Renderer
        celdaText = Gtk.CellRendererText()
        celdaText.set_property("editable", False)  # No podemos modificar esta celda
        columnaHotel = Gtk.TreeViewColumn('Alojamiento', celdaText, text=0)
        columnaHotel2 = Gtk.TreeViewColumn('Dirección', celdaText, text=1)
        columnaHote3 = Gtk.TreeViewColumn('Precio', celdaText, text=2)
        columnaHote4 = Gtk.TreeViewColumn('Ocupación', celdaText, text=3)
        columnaHote5 = Gtk.TreeViewColumn('Asterisco', celdaText, text=4)



        vista.append_column(columnaHotel)
        vista.append_column(columnaHotel2)
        vista.append_column(columnaHote3)
        vista.append_column(columnaHote4)
        vista.append_column(columnaHote5)


        box2=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        labelHotel=Gtk.Label()
        labelHotel.set_markup("Hotel")
        txtHotel=Gtk.Entry()
        labelDireccion=Gtk.Label()
        labelDireccion.set_markup("Dir")
        txtDireccion=Gtk.Entry()
        labelOcupacion=Gtk.Label()
        labelOcupacion.set_markup("Ocupacion")
        txtOcupacion=Gtk.Entry()
        labelCategoria=Gtk.Label()
        labelCategoria.set_markup("Categoria")
        cmbCategoria=Gtk.ComboBox()
        #labelNovo=Gtk.Label()
        #labelNovo.set_markup("Novo")
        btbNovo=Gtk.Button(label="Novo")
        labelMascotas=Gtk.Label()
        labelMascotas.set_markup("Mascotas")
        txtMascotas=Gtk.CheckButton()

        box2.pack_start(labelHotel, True, True, 0)
        box2.pack_start(txtHotel,True,True,0)
        box2.pack_start(labelDireccion, True, True, 0)
        box2.pack_start(txtDireccion, True, True, 0)
        box2.pack_start(labelOcupacion, True, True, 0)
        box2.pack_start(txtOcupacion, True, True, 0)
        box2.pack_start(labelCategoria, True, True, 0)
        box2.pack_start(cmbCategoria, True, True, 0)
        #box2.pack_start(labelNovo, True, True, 0)
        box2.pack_start(btbNovo, True, True, 0)
        box2.pack_start(labelMascotas, True, True, 0)
        box2.pack_start(txtMascotas, True, True, 0)

        box.add(box2)

        modeloCat=Gtk.ListStore(str,int)
        modeloCat.append(["*",1])
        modeloCat.append(["**", 1])
        modeloCat.append(["***", 1])
        modeloCat.append(["****", 1])
        modeloCat.append(["*****", 1])
        cmbCategoria.set_model(modeloCat)
        cmbCategoria.pack_start(celdaText,True)
        cmbCategoria.add_attribute(celdaText,"text",0)


        # permite añadir un control
        box.pack_start(vista, True, True, 0)
        self.add(box)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()





if __name__ == "__main__":
    WPrincipal1()
    Gtk.main()