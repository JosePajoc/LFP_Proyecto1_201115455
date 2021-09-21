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
def esLetra(caracter):
    valor = ord(caracter)                   #Convertir ASCII a entero
    if ((valor>= 65) and (valor<=90)) or ((valor>= 97) and (valor<=122)) or valor==165 or valor==164:
        return True
    else:
        return False

def esNumero(caracter):
    valor = ord(caracter)                   #Convertir ASCII a entero
    if ((valor>= 48) and (valor<=57)):
        return True
    else:
        return False

def imprimible(caracter):
    valor = ord(caracter)
    if (valor>=128 and valor<=239):
        return True
    else:
        return False

def analizar(entrada):
    fila = 1
    columna = 0
    estado = 0
    lexemaActual = ''

    for c in entrada:
        if estado == 0:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 1
            else:
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 1:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 1
            elif c == '=':
                lexemaActual = lexemaActual + c
                estado = 2
            elif ord(c) == 32 or ord(c) == 10:          #espacio en blanco ignorado
                pass
            else:
                if ord(c) == 9:     #enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 2:
            if c == '"':
                lexemaActual = lexemaActual + c
                estado = 3
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 7
            elif c == '{':
                lexemaActual = lexemaActual + c
                estado = 8
            elif esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 25
            elif ord(c) == 32 or ord(c) == 10:          #espacio en blanco ignorado
                pass
            else:
                if ord(c) == 9:     #enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 3:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif imprimible(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif c == ' ':
                lexemaActual = lexemaActual + c
                estado = 4
            else:
                if ord(c) == 10 or ord(c) == 9:     #enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 4:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif imprimible(c):
                lexemaActual = lexemaActual + c
                estado = 4
            elif c == ' ':
                lexemaActual = lexemaActual + c
                estado = 4
            elif c == '"':
                lexemaActual = lexemaActual + c
                estado = 5
            else:
                if ord(c) == 10 or ord(c) == 9:     #enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 5:
            if c == ";":
                lexemaActual = lexemaActual + c
                estado = 6
            else:
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 6:
            print('Se reconocio en S6: ' + lexemaActual + ' fila: ' , fila , ' col: ', columna-(len(lexemaActual)-1))
            
            if  ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                pass
                #print('Error lexico')
            lexemaActual = ''
            estado = 0
        elif estado == 7:
            if esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 7
            elif c == ';':
                lexemaActual = lexemaActual + c
                estado = 6
            else:
                if ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 8:
            if c == '[':
                lexemaActual = lexemaActual + c
                estado = 9
            elif ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                    pass
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 9:
            if esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 10
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 10:
            if esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 10
            elif c == ',':
                lexemaActual = lexemaActual + c
                estado = 11
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 11:
            if esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 12
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 12:
            if esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 12
            elif c == ',':
                lexemaActual = lexemaActual + c
                estado = 13
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 13:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 14
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 14:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 14
            elif c == ',':
                lexemaActual = lexemaActual + c
                estado = 15
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 15:
            if c == '#':
                lexemaActual = lexemaActual + c
                estado = 16
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 16:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 17
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 17
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 17:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 18
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 18
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 18:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 19
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 19
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 19:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 20
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 20
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 20:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 21
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 21
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 21:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 22
            elif esNumero(c):
                lexemaActual = lexemaActual + c
                estado = 22
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 22:
            if c == ']':
                lexemaActual = lexemaActual + c
                estado = 23
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 23:
            if c == ',':
                lexemaActual = lexemaActual + c
                estado = 8
            elif c == '}':
                lexemaActual = lexemaActual + c
                estado = 24
            elif ord(c) == 32 or ord(c) == 10 or ord(c) == 9:     #espacio en blanco, enter o tabulación
                    pass
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 24:
            if c == ';':
                lexemaActual = lexemaActual + c
                estado = 6
            else:
                lexemaActual = ''
                estado = 0
        elif estado == 25:                          
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 25
            elif c == ',':
                lexemaActual = lexemaActual + c
                estado = 26
            elif c == ';':
                lexemaActual = lexemaActual + c
                estado = 6
            elif ord(c) == 32:
                pass
            else:
                if ord(c) == 10 or ord(c) == 9:
                    pass
                lexemaActual = ''
                estado = 0
        elif estado == 26:
            if esLetra(c):
                lexemaActual = lexemaActual + c
                estado = 25
            elif ord(c) == 32:
                pass
            else:
                if ord(c) == 10 or ord(c) == 9:
                    pass
                lexemaActual = ''
                estado = 0

        # Control de filas y columnas
        if (ord(c) == 10):              #Salto de Línea
            columna = 0
            fila = fila + 1
            continue
        elif (ord(c) == 9):             #Tabulación Horizontal
            columna = columna +  4
            continue
        elif (ord(c) == 32):            #Espacio en blanco
            columna = columna + 1
            continue
        
        columna = columna + 1


def analizarImagenes():
    global imagenes
    for imagen in imagenes:
        #print(imagen)
        print('--------------------------------------------------------')
        analizar(imagen)


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
        archivoPXLA = archivoPXLA + '\n@@@@'                              #Agregando arrobas al final del archivo
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
