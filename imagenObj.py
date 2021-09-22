class imagenObjeto():
    def __init__(self, titulo, ancho, alto, filas, columnas, celdas, filtros):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.filtros = filtros
        self.celdasSep = []

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

    def verCeldas(self):
        return self.celdas
    
    def verFiltros(self):
        return self.filtros
    
    def separarCeldas(self):                #Split manual para cada cuatro comas
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
    
    def verCeldasSep(self):
        return self.celdasSep

