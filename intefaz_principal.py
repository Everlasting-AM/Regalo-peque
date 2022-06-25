import threading
from tkinter import *
from configuracion import *
from reproductor import *
from interfaz_Cola import controlador_cola as cc

CADENA_REPRODUCIENDO = "Reproduciendo: "
POSICION_INICIO = 0
NUM_COLUMNAS = 6
VOLUMEN_PREDETERMINADO = 50
confi = Configuracion()



def cambiar_a_botonPausa():
    misd.parado=False
    buttonPlay.config(image=imagen4)

def reproducirCancionLabel(song):
    if misd.parado:
        cambiar_a_botonPausa()
    reproducir(song)
    cancionVar.set(CADENA_REPRODUCIENDO+song)

def reproducirCancionAleatoria():
    reproducir_aleatoria()
    cancionVar.set(CADENA_REPRODUCIENDO+misd.cancion_actual)

# Funciones que implementan la funcionalidad de los botones
def marcarSiguienteRandom():
    if misd.siguiente=="Random":
        misd.siguiente = ""
        buttonNextRandom.config(image=imagen)
    else:
        if(misd.siguiente == "Bucle"):
            buttonBucle.config(image=imagen3)
        misd.siguiente = "Random"
        buttonNextRandom.config(image=imagen_boton_marcado_random)

def marcarBucle():
    if misd.siguiente == "Bucle":
        misd.siguiente = ""
        buttonBucle.config(image=imagen3)
    else:
        misd.siguiente = "Bucle"
        buttonBucle.config(image=imagen_boton_marcado_bucle)   

def pararReanudar():
    if misd.parado:
        cambiar_a_botonPausa()
        reanudarCancion()
    else:
        misd.parado = True
        buttonPlay.config(image=imagen2)
        pararCancion()

def iniciarCola(Cola):
    if Cola:
        reproducirCancionLabel(Cola.pop())

def elegir_siguiente_cancion():
    if misd.siguiente=="Bucle":
        reproducirCancionLabel(misd.cancion_actual)
    elif misd.siguiente=="Aleatorio":
        reproducirCancionAleatoria()
    elif confi.Cola:
        reproducirCancionLabel(confi.Cola.pop())
    else:
        pos = canciones.index(misd.cancion_actual)
        if(len(canciones)-1 == pos):
            lista.activate(0)
        else:  
            lista.activate(pos+1)

def prepararCancion(indice):
    if indice:
        reproducirCancionLabel(canciones[indice[0]])
# Creación de la lista de selección de canciones y su scrollbar
def creaLista(frame):
    # Incluimos la listbox
    global lista
    lista = Listbox(frame,width=100, font=(FUENTE_NORMAL,10))
    lista.bind('<<ListboxSelect>>', lambda event: prepararCancion(lista.curselection()))
    for i in range(0,len(canciones)):
        lista.insert(i,canciones[i])

    lista.grid(row=1, column=0,columnspan=3, padx=10, pady=10, sticky="NS")

    # Incluimos la barra de desplazamiento
    scroll_list = Scrollbar(frame)
    scroll_list.grid(row=1, column=4, padx=5, pady=5, sticky=NS)
    lista.config(yscrollcommand= scroll_list.set)
    scroll_list.config(command=lista.yview)

def crearBotones(frame):
    global imagen                             # Si no se usa el garbage se la trinca
    global imagen2 
    global imagen3
    global imagen4
    global imagen_boton_marcado_bucle
    global imagen_boton_marcado_random
    
    
    imagen2 = PhotoImage(file= resource_path("imagenes/boton-de-play.png"))
    imagen3 = PhotoImage(file= resource_path("imagenes/boton-bucle.png"))
    imagen4 = PhotoImage(file= resource_path('imagenes/boton-circular-de-pausa.png'))
    imagen_boton_marcado_bucle = PhotoImage(file= resource_path("imagenes/boton-bucle-seleccionado.png"))
    imagen_boton_marcado_random = PhotoImage(file= resource_path("imagenes/boton-next-aleatorio-seleccionado.png"))

    fbotones = Frame(frame)
    fbotones.grid(row = 5, column=0, columnspan=NUM_COLUMNAS)

    # Función lambda para crear los botones
    nuevoBotonImagen = lambda photo: Button(fbotones, image=photo, borderwidth=0)
    
    global buttonNextRandom
    imagen = PhotoImage(file= resource_path("imagenes/boton-next-aleatorio.png")) 
    buttonNextRandom = Button(fbotones, image=imagen, borderwidth=0)
    buttonNextRandom.config(command=lambda:marcarSiguienteRandom())
    buttonNextRandom.grid(row=0, column=0, sticky=W, padx=30, pady=10)

    global buttonPlay
    buttonPlay = nuevoBotonImagen(imagen2)
    buttonPlay.config(command=lambda:pararReanudar())
    buttonPlay.grid(row=0, column=1, sticky=E, padx=30, pady=10)
    
    global buttonBucle
    buttonBucle = nuevoBotonImagen(imagen3)
    buttonBucle.config(command=lambda:marcarBucle())
    buttonBucle.grid(row=0,column=2,sticky=W+E, padx=30, pady=10)

def openColaWindow():
    rt = Toplevel(root)
    rt.iconbitmap(resource_path('imagenes\corazon-rojo.ico'))
    pestanaCola = cc(rt, confi)
    

# Función con la que escuchamos constantemente por si sucede algún evento
def check_event():
    while(True):
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                print("Se ha parado la canción")
                elegir_siguiente_cancion()
            elif event.type == PESTANA_COLA_OFF:
                iniciarCola(confi.Cola)
             
iniciarReproductor()
root = Tk()
root.iconbitmap(resource_path('imagenes\corazon-rojo.ico'))
root.config(cursor="heart")
root.title("Tu reproductor de música")
fprincipal = Frame(root)
fprincipal.pack(fill='x')
# Incluimos el título
titulo = Label(fprincipal, text= "Reproductor de mi bebe", font = (FUENTE_BOTONES, 16))
titulo.grid(row=0, column=0, columnspan=NUM_COLUMNAS, padx=50, pady=10, sticky=W+E)

# Insertamos la nota
creaLista(fprincipal)

# Insertamos la label 
cancionVar = StringVar()
cancionVar.set("Aún no se está reproduciendo nada")
texto_cancion_actual = Label(fprincipal, textvariable=cancionVar, font = (FUENTE_BOTONES, 14))
texto_cancion_actual.grid(row=2, column=0, columnspan=NUM_COLUMNAS, sticky=W+E, padx = 10, pady = 10)

# Insertamos el botón para que la canción sea aleatoria
boton_elegir_random = Button(fprincipal, text = "Elegir aleatoria",  font = (FUENTE_BOTONES, 14), command=lambda:reproducirCancionAleatoria())
boton_elegir_random.grid(row = 3, column=0, columnspan=NUM_COLUMNAS, sticky=W+E, padx=10, pady=10)
configurar_boton(boton_elegir_random)
# Insertamos el botón  cola 
Cola = []
botonCola = Button(fprincipal, text="Crear cola", font=(FUENTE_BOTONES, 14), command=lambda:openColaWindow())
configurar_boton(botonCola)
botonCola.grid(row=4, column=0, columnspan=NUM_COLUMNAS, sticky=W+E, padx=10, pady=10)

# Insertamos el frame para los botones de siguiente random, parar y repetir en bucle
crearBotones(fprincipal)

# Insertamos finalmente el scale para determinar el volumen
volumen = IntVar()
volumen.set(VOLUMEN_PREDETERMINADO)
medidor = Scale(fprincipal, variable= volumen, orient= HORIZONTAL, command=lambda vol:setVolume(float(vol)/100), relief="ridge")
medidor.grid(row = 6, column=0, columnspan=NUM_COLUMNAS, sticky=W+E, padx=10, pady = 10)

hiloEscucharEventos = threading.Thread(target = check_event, daemon=True)
hiloEscucharEventos.start()
root.mainloop()
