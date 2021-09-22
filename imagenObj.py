class imagenObjeto():
    def __init__(self, titulo, ancho, alto, filas, columnas, celdas, filtros):
        self.titulo = titulo
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas
        self.celdas = celdas
        self.filtros = filtros

    def verTitulo(self):
        return self.titulo

    def verCeldas(self):
        return self.celdas

#print('TITULO = "EJEMPLO"'.startswith('TITULO'))