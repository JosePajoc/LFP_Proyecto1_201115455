from graphviz import render

class imagenObjeto():
    def __init__(self, titulo, ancho, alto, filas, columnas, celdas, filtros):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas            #celdas en una sola cadena
        self.filtros = filtros
        self.celdasSep = []             #celdas separadas por posiciones
        self.imagen = None

    def verTitulo(self):
        return self.titulo
    
    def verAncho(self):
        return self.ancho
    
    def verAlto(self):
        return self.alto
    
    def verFilas(self):
        return self.filas
    
    def verColumnas(self):
        return self.columnas

    def verCeldas(self):                    #celdas en una sola cadena
        return self.celdas
    
    def verFiltros(self):
        return self.filtros
    
    def separarCeldas(self):                
        #FASE 1
        #Split manual para cada cuatro comas, separar celdas en una lista
        temporal = ''
        control = 0
        if self.celdas !='':
            for c in self.celdas:
                if c == ',':
                    control = control + 1
                if control == 4:
                    self.celdasSep.append(temporal)
                    temporal = ''
                    control = 0
                else:
                    temporal = temporal + c
        #FASE 2
        #creando matriz con dimensiones definidas y llenando con letra a
        self.imagen = [['a' for co in range(self.columnas)] for fi in range(self.filas)]    
        
        #FASE 3
        #extraer valores de cada celda y llenar matriz para dibujar
        for celda in self.celdasSep:        
            valor = ''
            x = None
            y = None
            estado = None
            color = None
            for c in range(1,len(celda)):
                if celda[c] == ',' or celda[c] == ']':
                    if x == None and y == None and estado ==None and color == None:
                        x = int(valor)
                        valor = ''
                    elif x != None and y == None and estado ==None and color == None:
                        y = int(valor)
                        valor = ''
                    elif x != None and y != None and estado ==None and color == None:
                        estado = valor
                        valor = ''
                    elif x != None and y != None and estado !=None and color == None:
                        color = valor
                        valor = ''
                else:
                    valor = valor + celda[c]                    
            #print('x: ', x, ' Y: ',y, ' estado: ', estado, ' color: ', color)
            if estado == 'TRUE':
                self.imagen[y][x] = color
            else:
                self.imagen[y][x] = '#FFFFFF'
        
        self.titulo = self.titulo.replace('"', '')
        self.crearGrafo(self.titulo, 'ORIGINAL')
        self.crearHTML(self.titulo, 'ORIGINAL', self.ancho, self.alto)
        
        if 'MIRRORX' in self.filtros:
            self.crearGrafo('Mirror_x_' + self.titulo, 'MIRRORX')
            self.crearHTML('Mirror_x_' + self.titulo, 'MIRRORX', self.ancho, self.alto)
        if 'MIRRORY' in self.filtros:
            self.crearGrafo('Mirror_y_' + self.titulo, 'MIRRORY')
            self.crearHTML('Mirror_y_' + self.titulo, 'MIRRORY', self.ancho, self.alto)
        if 'DOUBLEMIRROR' in self.filtros:
            self.crearGrafo('Double_Mirror_' + self.titulo, 'DOUBLEMIRROR')
            self.crearHTML('Double_Mirror_' + self.titulo, 'DOUBLEMIRROR', self.ancho, self.alto)
        #print(self.imagen)

    
    def crearGrafo(self, tituloImg, tipo):
        #Crear imagen original y por el tipo de filtro en graphviz
        nombreGrafo = 'imagenes/' + tituloImg + '.dot'
        salidaImagen = open(nombreGrafo, 'w')
        salidaImagen.write('digraph G { \n')
        salidaImagen.write('node [shape=plaintext] \n')
        salidaImagen.write('a [label=<<table border="0" cellborder="1" cellspacing="0"> \n')

        if tipo == 'ORIGINAL':
            for y in range(self.filas):
                salidaImagen.write('<tr>\n')

                for x in range(self.columnas):
                    salidaImagen.write('<td width="20" height="20" bgcolor="' + self.imagen[y][x] + '"></td>')

                salidaImagen.write('</tr>\n')
        
        elif tipo == 'MIRRORX':
            for y in range(self.filas):
                col = self.columnas - 1                
                salidaImagen.write('<tr>\n')

                while col > -1:
                    salidaImagen.write('<td width="20" height="20" bgcolor="' + self.imagen[y][col] + '"></td>')
                    col = col - 1
                salidaImagen.write('</tr>\n')
        
        elif tipo == 'MIRRORY':
            fil = self.filas - 1
            while fil > -1:
                salidaImagen.write('<tr>\n')

                for x in range(self.columnas):
                    salidaImagen.write('<td width="20" height="20" bgcolor="' + self.imagen[fil][x] + '"></td>')
                fil = fil - 1
                salidaImagen.write('</tr>\n')
        
        elif tipo =='DOUBLEMIRROR':
            fil = self.filas - 1
            while fil > -1:
                salidaImagen.write('<tr>\n')

                col = self.columnas - 1
                while col > -1:
                    salidaImagen.write('<td width="20" height="20" bgcolor="' + self.imagen[fil][col] + '"></td>') #SEGUIR
                    col = col - 1
                fil = fil - 1

                salidaImagen.write('</tr>\n')

        salidaImagen.write('</table>>]; \n')
        salidaImagen.write('}')
        salidaImagen.close()
        render('dot', 'png', nombreGrafo)                                #Renderizar el archivo DOT escrito


    def crearHTML(self, tituloImg, tipo, ancho, alto):
        archivoCSS = open("html/estilos.css", "w")
        contenidoCSS = """html {   font-size: 20px; font-family: 'Open Sans', sans-serif; } \n
                    h1 { font-size: 60px; text-align: center; } \n
                    p, li {   font-size: 16px;   line-height: 2;   letter-spacing: 1px; }\n
                    html { background-color: #00539F; }
                    body { width: 1100px; margin: 0 auto; background-color: #FF9500; padding: 0 20px 20px 20px; border: 5px solid black; }
                    h1 { margin: 0; padding: 20px 0; color: #00539F; text-shadow: 3px 3px 1px black; }"""
        archivoCSS.write(contenidoCSS)
        archivoCSS.close()

        nombreGrafo = 'html/' + tituloImg + '.html'
        archivoHTML = open(nombreGrafo, 'w')
        archivoHTML.write('<!doctype html> \n')
        archivoHTML.write('<html> \n')
        archivoHTML.write('<head>\n')
        archivoHTML.write('\t<title>' + tituloImg +'</title>\n')
        archivoHTML.write('\t<link href="estilos.css" rel="stylesheet" type="text/css">\n')
        archivoHTML.write('</head>\n')
        archivoHTML.write("<body>\n")
        archivoHTML.write('<h1>' + tituloImg + '</h1>\n')
   
        archivoHTML.write('<h3> tipo de filtro: ' + tipo + '</h3>\n')
        archivoHTML.write('<img src="../imagenes/' + tituloImg + '.dot.png" width="' + str(ancho) + '" heigth="' + str(alto) + '">\n')
        
        archivoHTML.write("</body>\n")
        archivoHTML.write("</html>\n")
        archivoHTML.close()

    
    def verCeldasSep(self):
        return self.celdasSep
