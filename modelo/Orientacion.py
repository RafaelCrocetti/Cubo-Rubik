class Orientacion:
    def __init__(self,colores,caras):
        self.colores=colores
        self.caras=caras

    def obtenerColorEnCara(self,cara):
        for i in range(len(self.caras)):
            if cara==self.caras[i]:
                return self.colores[i]
    def obtenerCaraDelColor(self,color):
        for i in range(len(self.colores)):
            if color==self.colores[i]:
                return self.caras[i]
    def obtenerNumeroColor(self, color):
        colores=["Verde","Amarillo","Rojo","Blanco","Naranja","Azul","Sin Color"]
        for i in range(len(colores)):
            if(color==colores[i]):
                return i+1

