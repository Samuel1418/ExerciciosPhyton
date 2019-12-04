import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exercicio1")

        caixaprincipal=Gtk.Box()
        caixaprincipal=Gtk.Box(orientation= Gtk.Orientation.VERTICAL)

        caixa1 = Gtk.Box()
        ''' Esto seria para hacerlo con el codigo 
        frmOpcions=Gtk.Frame()
        frmOpcions.set_label("Opcións")


        caixa1Interior1 = Gtk.Box()
        grid = Grid1()
        caixa1Interior1.add(grid)
        '''

        builder=Gtk.Builder()    #mucho mas facil, solo hace falta añadirlo
        builder.add_from_file("PruebaCombi.glade")
        self.txtData=builder.get_object("txtData")
        grade = builder.get_object("grdGrade") #Y luego seleccionar la ventana para poder hacer el add
        txtVoosDisp= Gtk.TextView() #Esto se añade al frame abajo para que me muestre ahí
        self.buffertxt=txtVoosDisp.get_buffer()
        fiestraScroll= Gtk.ScrolledWindow()
        fiestraScroll.set_hexpand(True)
        fiestraScroll.set_vexpand(True)
        fiestraScroll.add(txtVoosDisp)

        self.comboDende = builder.get_object("cmbDende")#Estos los cojo de glade.Los que tengo abajo en la clase no se estan usando
        self.txtData = builder.get_object("txtData")
        self.cmbAta=builder.get_object("cmbAta") #No lo metemos en sinais porque solo es para ver que lo muestra, no para que realiza algo
        self.cmbRadioButton=builder.get_object("cmbRadio")
        self.chkPrioridade=builder.get_object("chkPrioridade")
        self.chkMaletaMan = builder.get_object("chkMaletaMan")
        self.chkSalidaEmergencia = builder.get_object("chkSalidaEmergencia")


        sinais={"on_txtData_activate": self.on_txtData_activate,"on_cmbDende_changed":self.on_cmbDende_changed,"on_rtbs_toggle":self.on_rtbs_toggle,self.on_chkSalidaEmergencia_toggled:"on_chkSalidaEmergencia_toggled",
                self.on_chkMaletaMan_toggled:"on_chkMaletaMan_toggled",self.on_chkPrioridade_toggled:"on_chkPrioridade_toggled"} #Se hace fuera del constructor, esta abajo

        builder.connect_signals(sinais)

        lista_destinos= Gtk.ListStore(int,str,str)#el numero en que se muestran y dos string para porner como si fuera un aeropuerto pero se puede poner sólo un string
        lista_destinos.append([1,"Vigo","Vgo"])
        lista_destinos.append([2, "Cambados", "Cmb"])
        lista_destinos.append([3, "Santiago de compostela", "Stg"])
        lista_destinos.append([4, "Barcelona", "Bcn"])
        self.comboDende.set_model(lista_destinos) #NO vale añadir con el add
        celdaTexto= Gtk.CellRendererText()#cada parte del combo es un cell text
        self.comboDende.pack_start(celdaTexto,True) #añadimos la celda
        self.comboDende.add_attribute(celdaTexto,"text",1) #elegimos que nos muestre el texto de la pimera columna. Si ponemos 2 muestra las abreviaturas

        lisa_iconos= Gtk.ListStore(str,str)
        lisa_iconos.append(["Pamplona","documento-new"])
        lisa_iconos.append(["Valencia", "documento-new"])
        lisa_iconos.append(["Cadiz", "documento-new"])
        self.cmbAta.set_model(lisa_iconos)
        #self.cmbAta.pack_start(celdaTexto,True)
        #self.cmbAta.add_attribute(celdaTexto,"text",1)
        celdaUmaxe=Gtk.CellRendererPixbuf()  #COn esto podemos poner iconos
        self.cmbAta.pack_start(celdaUmaxe, True)
        self.cmbAta.add_attribute(celdaUmaxe, "icon_name",1)



        caixa1Interior2 = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        #caixa1Interior2.add(frmOpcions)
        rbtPrimeira= Gtk.RadioButton("Primeira")
        rbtNegocios = Gtk.RadioButton("Negocios")
        rbtTurista = Gtk.RadioButton("Turista")
        rbtNegocios.join_group(rbtPrimeira) #Que el radio button empiece en rbtPrimeira
        rbtTurista.join_group(rbtPrimeira)
        rbtTurista.connect("toggled",self.on_rtbs_toggle,"Turista")  #Añadimos los 3 al toggle
        rbtNegocios.connect("toggled", self.on_rtbs_toggle,"Negocios")
        rbtPrimeira.connect("toggled", self.on_rtbs_toggle,"Primeira")

        caixa1Interior2.add(rbtPrimeira)
        caixa1Interior2.add(rbtNegocios)
        caixa1Interior2.add(rbtTurista)
        caixa1.add(grade)
        caixa1.add(caixa1Interior2)




        caixa2 = Gtk.Box()
        frame2 = Gtk.Frame()
        frame2.set_label("Voos dispoñibles")
        #tctVoosDisp= Gtk.TextView()
        #frame2.add(tctVoosDisp)
        frame2.add(fiestraScroll) #Si lo de arriba esta activado, no deja hacer el enter para pasar el texto
        caixa2.add(frame2)


        caixa3 = Gtk.Box()




        botones= Botones()
        caixa3.add(botones)


        caixaprincipal.add(caixa1)
        caixaprincipal.add(caixa2)
        caixaprincipal.add(caixa3)
        self.add(caixaprincipal)


        self.connect("destroy", Gtk.main_quit)

        self.show_all()

    def on_txtData_activate(self,control):
        fin= self.buffertxt.get_end_iter()
        self.buffertxt.insert(fin, self.txtData.get_text(),-1)
        """ Esto es con buffer pero me daba error
        seleccion = self.buffertxt.get_selection_bounds()
        if len(seleccion) != 0:
            self.buffertxt.delete(seleccion[0], seleccion[1])
            self.buffertxt.insert_markup(seleccion[0], "<b>" + self.txtData.get_text() + "</b>")
        else:
            fin = self.buffertxt.get_end_iter()
            self.buffertxt.insert_markup(fin, "<b>" + self.txtData.get_text() + "</b>", -1)
            self.buffertxt.insert(fin, "\n", -1)
        """

       # cadea = self.txtData.get_text()
       # print (cadea)
       # self.buffertxt.set_text(cadea)


    def on_cmbDende_changed(self,combo):
        punteiro= self.comboDende.get_active_iter()
        if punteiro is not None:
            modelo=combo.get_model() #para tener acceso a datos
            self.buffertxt.set_text("O aeroporto seleccionado é: "+modelo[punteiro][1]+"("+modelo[punteiro][2]+")")


    def on_rtbs_toggle(self,control, nome):
        if control.get_active():
            fin = self.buffertxt.get_end_iter()
            self.txtData.set_text("")
            self.buffertxt.insert(fin,"activado o radiobutton "+nome)

    def on_chkPrioridade_toggled(self,control):
        texto=self.txtData.get_text()+"\n"
        indice=self.comboDende.get_active_iter()
        destino=self.comboDende.get_model(indice[1])
        if self.rbtPrimeira.get_active():
            clase="Primeira"
        elif self.rbtNegocios.get_active():
            clase="Negocios"
        else:
            clase="Turista"
        texto= texto+" Clase "+clase+" Destino "+destino+""
        self.txtData.set_text(texto)

    def on_chkSalidaEmergencia_toggled(self,control):
        texto=self.txtData.get_text()+"\n"
        indice=self.comboDende.get_active_iter()
        destino=self.comboDende.get_model(indice[1])
        if self.rbtPrimeira.get_active():
            clase="Primeira"
        elif self.rbtNegocios.get_active():
            clase="Negocios"
        else:
            clase="Turista"
        texto= texto+" Clase "+clase+" Destino "+destino+""
        self.txtData.set_text(texto)

    def on_chkMaletaMan_toggled(self,control):
        texto=self.txtData.get_text()+"\n"
        indice=self.comboDende.get_active_iter()
        destino=self.comboDende.get_model(indice[1])
        if self.rbtPrimeira.get_active():
            clase="Primeira"
        elif self.rbtNegocios.get_active():
            clase="Negocios"
        else:
            clase="Turista"
        texto= texto+" Clase "+clase+" Destino "+destino+""
        self.txtData.set_text(texto)

class Grid1(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)

        etiquetaData= Gtk.Label()
        etiquetaData.set_markup("Data:")

        etiquetaDende = Gtk.Label()
        etiquetaDende.set_markup("Dende:")

        etiquetaAta = Gtk.Label()
        etiquetaAta.set_markup("Ata:")

        txtData= Gtk.Entry()

        comboDende= Gtk.ComboBox()

        comboAta= Gtk.ComboBox()

        self.add(etiquetaData)
        self.attach(txtData, 1, 0, 1, 1)  # pos de FILA, COLUMNA y cuanto ocupa en horizontal y vertical
        self.attach(etiquetaDende,-1,2,2,1)
        self.attach(comboDende, 1, 2, 2, 1)  # pos de FILA, COLUMNA y cuanto ocupa en horizontal y vertical
        self.attach(etiquetaAta,-1,3,2,1)
        self.attach(comboAta,1, 3, 2, 1)  # pos de FILA, COLUMNA y cuanto ocupa en horizontal y vertical

class Botones(Gtk.Grid):

    def __init__(self):
        Gtk.Grid.__init__(self)

        boton1 = Gtk.Button(label="Buscar")
        boton2 = Gtk.Button(label="Comprar")
        boton3 = Gtk.Button(label="Salir")
        self.add(boton1)
        self.attach(boton2, 1, 0, 2, 1) #pos de COLUMNA, FILA y cuanto ocupa en horizontal y vertical
        self.attach(boton3, 3, 0, 2, 1)

        caixa= Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL)



if __name__ == "__main__":
    Fiestra()
    Gtk.main()