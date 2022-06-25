from tkinter import *
from tkinter import ttk
import sys
import os

FUENTE_BOTONES = "Franklin Gothic Demi"
FUENTE_NORMAL = "Franklin Gothic Medium"
FUENTE_TITULOS = "Franklin Gothic Heavy"
TAMANO_LTITULO = 0
TAMANO_LBOTONES = 14
TAMANO_LNORMAL = 0
BORDES_BOTONES = ""
BG_FRAME = ""
BG_BOTONES = ""

def configurar_boton(boton):
    boton.config(relief="ridge", activeforeground="red", borderwidth=4, activebackground = "black", bg = "black", fg = "white")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Configuracion:
    def __init__(self):
        self.Cola = []

