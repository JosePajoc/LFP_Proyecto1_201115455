from tkinter import filedialog                      #Módulo para abrir ventana de selección
from tkinter import messagebox                      #Módulo para cuadros de mensaje
from tkinter import *                               #Módulo para entorno gráfico
from PIL import Image, ImageTk                      #Instalar módulo, pip install Pillow, para usar imagenes con más opciones
import re                                           #Módulo de expresiones regulares
import webbrowser                                   #Módulo para abrir automaticamente el navegador

#-----------------------------------------Variables globales-----------------------------------------------------
rutaArchivo = ''
archivoPXLA = None
imagenes = []

#-------------------------------------------Ventana inicial-----------------------------------------------------------
ventanaInicial = Tk()                                           #Objeto de tipo ventana
ventanaInicial.title('Bitxelart')
ventanaInicial.resizable(False, False)                          #No permitir cambios al ancho y alto de la ventana

marcoInicial = Frame(ventanaInicial, width="800", height="550")
marcoInicial.pack()                                             #Marco agregado a la ventana

#------------------------------------------Fuciones--------------------------------------------------------------
def analizarImagenes():
    global imagenes
    for imagen in imagenes:
        print(imagen)
        print('--------------------------------------------------------')

def habilitarBotones():
    global rutaArchivo
    btnCargar = Button(marcoInicial, text='Cargar', state=DISABLED)
    btnCargar.place(x=50, y=20)
    btnAnalizar = Button(marcoInicial, text='Analizar archivo', command=analizarImagenes)
    btnAnalizar.place(x=120, y=20)
    btnReportes = Button(marcoInicial, text='Ver reportes')
    btnReportes.place(x=240, y=20)
    btnSeleccionarImg = Button(marcoInicial, text='Seleccionar imagen')
    btnSeleccionarImg.place(x=330, y=20)
    btnVerImg = Button(marcoInicial, text='Ver imagen')
    btnVerImg.place(x=460, y=20)
    btnOriginal = Button(marcoInicial, text='ORIGINAL')
    btnOriginal.place(x=60, y=170)
    btnMirrorX = Button(marcoInicial, text='MirrorX')
    btnMirrorX.place(x=60, y=220)
    btnMirrorY = Button(marcoInicial, text='MirrorY')
    btnMirrorY.place(x=60, y=270)
    btnDoubleMirror = Button(marcoInicial, text='DoubleMirror')
    btnDoubleMirror.place(x=60, y=320)

def separarImagenes(entrada):
    global imagenes
    cadena = ''
    contador = 0
    for c in entrada:
        if c == '@':
            contador = contador + 1
        else:
            cadena = cadena + c
        if contador == 4:
            imagenes.append(cadena)
            cadena = ''
            contador = 0
    
def abrirArchivo():
    global rutaArchivo, archivoPXLA

    rutaArchivo = filedialog.askopenfilename(title = "Seleccionar archivo XML")
    extension = re.findall('(\.pxla)$', rutaArchivo)                    #<------------ ver extensión valida
    
    if rutaArchivo == '':
        messagebox.showinfo('Error','No se selecciono nigún archivo')
    elif len(extension)>0 and extension[0] == '.pxla':
        archivoCargado = open(rutaArchivo, 'r')
        archivoPXLA = archivoCargado.read()
        archivoPXLA = archivoPXLA + '@@@@'                              #Agregando arrobas al final del archivo
        archivoCargado.close()
        messagebox.showinfo('Información','Cargado con éxito')
        habilitarBotones()
        separarImagenes(archivoPXLA)
    else:
        messagebox.showinfo('Error','El archivo seleccionado no posee extisón \'.pxla\'')
        rutaArchivo = ''


#------------------------------------------ Widgets de la ventana inicial----------------------------------------
btnCargar = Button(marcoInicial, text='Cargar', command=abrirArchivo)
btnCargar.place(x=50, y=20)
btnAnalizar = Button(marcoInicial, text='Analizar archivo', state=DISABLED)
btnAnalizar.place(x=120, y=20)
btnReportes = Button(marcoInicial, text='Ver reportes', state=DISABLED)
btnReportes.place(x=240, y=20)
btnSeleccionarImg = Button(marcoInicial, text='Seleccionar imagen', state=DISABLED)
btnSeleccionarImg.place(x=330, y=20)
btnVerImg = Button(marcoInicial, text='Ver imagen', state=DISABLED)
btnVerImg.place(x=460, y=20)
btnOriginal = Button(marcoInicial, text='ORIGINAL', state=DISABLED)
btnOriginal.place(x=60, y=170)
btnMirrorX = Button(marcoInicial, text='MirrorX', state=DISABLED)
btnMirrorX.place(x=60, y=220)
btnMirrorY = Button(marcoInicial, text='MirrorY', state=DISABLED)
btnMirrorY.place(x=60, y=270)
btnDoubleMirror = Button(marcoInicial, text='DoubleMirror', state=DISABLED)
btnDoubleMirror.place(x=60, y=320)

noImagen1 = Image.open('imagenes/no-imagen.png')
tamanoImagen1 = noImagen1.resize((400, 350))
renderizadoImagen1 = ImageTk.PhotoImage(tamanoImagen1)
imagenlbl = Label(marcoInicial, image=renderizadoImagen1)
imagenlbl.image = renderizadoImagen1
imagenlbl.place(x=250, y=90)

ventanaInicial.mainloop()                                       #Ejecutar ventana hasta cerrar
