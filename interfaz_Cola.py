from tkinter import *
from reproductor import *
from configuracion import resource_path

FUENTE_BOTONES = "Cascadia Mono SemiBold"
FUENTE_NORMAL = "Cascadia Mono Light"

class controlador_cola:

    def __init__(self, frame, confi):
        self.frame = frame
        self.lista_canciones_grafica= Listbox()
        self.texto_cola= Listbox()
        self.boton_home = Button()
        self.button_iniciar = Button()
        self.confi = confi
        self.insertControlerButtons()

    def insertControlerButtons(self):
        # Insertamos el frame donde ira la primera lista    
        frame_lista = Frame(self.frame)
        frame_lista.pack(fill='x', expand=1)

        # Incluimos el botón de regreso al menú
        global photo
        photo = PhotoImage(file=resource_path("imagenes/boton-regresar-menu.png"))
        self.boton_home = Button(frame_lista, image= photo, bd = 0, command= lambda:self.salir())
        self.boton_home.place(relx=0, rely=0)

        # Incluimos la label
        titulo_lista = Label(frame_lista,text = "Esta es tu alucinante lista de canciones: ", font=(FUENTE_BOTONES, 14))
        titulo_lista.grid(row=0, column=0, columnspan=4, padx=50, pady=10, sticky=W+E)

        # Incluimos la listbox
        self.lista_canciones_grafica = Listbox(frame_lista,width=65, font=(FUENTE_NORMAL,10))

        for i in range(0,len(canciones)):
            self.lista_canciones_grafica.insert(i,canciones[i])

        self.lista_canciones_grafica.grid(row=1, column=0, padx=10, pady=10, sticky="NS")

        # Incluimos la barra de desplazamiento
        scroll_list = Scrollbar(frame_lista)
        scroll_list.grid(row=1, column=1, padx=5, pady=5, sticky=NS)
        self.lista_canciones_grafica.config(yscrollcommand= scroll_list.set)
        scroll_list.config(command=self.lista_canciones_grafica.yview)

        # Insertamos un segundo texto y scrollbarr
        self.texto_cola = Listbox(frame_lista, width=65, font=(FUENTE_NORMAL,10))
        self.texto_cola.grid(row=1, column=3, padx=10, pady=10, sticky=NSEW)

        # Vamos a incluir dos botones para agregar o eliminar canciones de la cola cuando esta se esté creando
        framebotones = Frame(frame_lista)
        insertar = Button(framebotones, text= "Insertar", font=(FUENTE_BOTONES,12), command=lambda:self.insertar_cola())
        eliminar = Button(framebotones, text= "Eliminar", padx=10, pady=10, font=(FUENTE_BOTONES,12), command=lambda:self.eliminar_cola())
        
        insertar.grid(row=0, column=0, padx=10, pady=10)
        eliminar.grid(row=1, column=0, padx=10, pady=10)
        
        framebotones.grid(row=1, column=2)
        self.button_iniciar = Button(framebotones, text="Iniciar", padx=10, pady=10, font=(FUENTE_BOTONES,12), command=lambda:self.salirGuardar())
        self.button_iniciar.grid(row=2, column=0)

        #Incluimos el scrollbar de la segunda lista
        scoll_cola = Scrollbar(frame_lista)
        scoll_cola.grid(row =1, column=4, padx=5, pady=5,sticky=NS) 
        scoll_cola.config(command= self.texto_cola.yview)
        self.texto_cola.config(yscrollcommand=scroll_list.set)

        self.frame.mainloop()

    def insertar_cola(self):
        # Obtenemos la canción seleccionada e insertamos en la lista de la cola
        indice = self.lista_canciones_grafica.curselection()
        if indice:
            self.texto_cola.insert(END, self.lista_canciones_grafica.get(indice[0]))

    def eliminar_cola(self):
        # Get the index of the song we want to delete
        index = self.texto_cola.curselection()
        if index:
            self.texto_cola.delete(index[0])

    def salirGuardar(self):
        self.confi.Cola = list(self.texto_cola.get(0,END))
        self.confi.Cola.reverse()
        pygame.event.post(pygame.event.Event(PESTANA_COLA_OFF))        
        self.salir()

    def salir(self):
        self.frame.destroy()
        