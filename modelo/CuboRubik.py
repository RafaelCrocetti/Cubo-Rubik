import math
from modelo.Posicion import Posicion
from modelo.Orientacion import Orientacion
from modelo.SubCubo import SubCubo
class CuboRubik:
    def __init__(self):
        self.SubCubos=[]

        # se adapta la codificacion para las caras:
        # 1: posterior
        # 2: izquierda
        # 3: superior
        # 4: derecha
        # 5: inferior
        # 6: frontal
        # 7: ninguna
        # las caras estan enumeradas como un cubo desarrollado en un plano
        # y sus correspondiente colores abajo se calculan restandole
        # 1 al numero de cara y dara el indice correcto en este vector
        # para la posicionObjetivo
        # la idea es llenar la lista de subcubos con filas que lenen un
        # plano con tres filas y el cubo con tres planos
        colores=["Verde","Amarillo","Rojo","Blanco","Naranja","Azul","Sin Color"]
        id=0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    id=id+1
                    if id==1:
                        carasSubCubo = [2, 5, 6]
                    elif id==2:
                        carasSubCubo = [ 5, 6]
                    elif id==3:
                        carasSubCubo = [ 4, 5, 6]
                    elif id==4:
                        carasSubCubo=[2, 5]
                    elif id==5:
                        carasSubCubo=[5]
                    elif id==6:
                        carasSubCubo=[4,5]
                    elif id==7:
                        carasSubCubo=[1,2,5]
                    elif id==8:
                        carasSubCubo=[1,5]
                    elif id==9:
                        carasSubCubo=[1,4,5]
                    elif id==10:
                        carasSubCubo=[2,6]
                    elif id==11:
                        carasSubCubo=[6]
                    elif id==12:
                        carasSubCubo=[4,6]
                    elif id==13:
                        carasSubCubo=[2]
                    elif id==14:
                        carasSubCubo=[7]
                    elif id==15:
                        carasSubCubo=[4]
                    elif id==16:
                        carasSubCubo=[1,2]
                    elif id==17:
                        carasSubCubo=[1]
                    elif id==18:
                        carasSubCubo=[1,4]
                    elif id==19:
                        carasSubCubo=[2,3,6]
                    elif id==20:
                        carasSubCubo=[3,6]
                    elif id==21:
                        carasSubCubo=[3,4,6]
                    elif id==22:
                        carasSubCubo=[2,3]
                    elif id==23:
                        carasSubCubo=[3]
                    elif id==24:
                        carasSubCubo=[3,4]
                    elif id==25:
                        carasSubCubo=[1,2,3]
                    elif id==26:
                        carasSubCubo=[1,3]
                    elif id==27:
                        carasSubCubo=[1,3,4]



                    if len(carasSubCubo)==3:
                        coloresSubCubo = [colores[carasSubCubo[0] - 1], colores[carasSubCubo[1] - 1],
                                      colores[carasSubCubo[2] - 1]]
                        tipo="Esquina"
                    elif len(carasSubCubo)==2:
                        coloresSubCubo = [colores[carasSubCubo[0] - 1], colores[carasSubCubo[1] - 1]]
                        tipo="Arista"
                    elif len(carasSubCubo)==1:
                        tipo="Centro"
                        coloresSubCubo = [colores[carasSubCubo[0] - 1]]

                    posicionActual=Posicion(i,j,k)
                    posicionObjetivo=Posicion(i,j,k)


                    orientacionActual = Orientacion(coloresSubCubo,carasSubCubo)
                    orientacionObjetivo = Orientacion(coloresSubCubo,carasSubCubo)
                    subCubo = SubCubo(id, posicionActual, posicionObjetivo, orientacionActual, orientacionObjetivo,
                                      tipo)
                    self.SubCubos.append(subCubo)

    def print(self):

        for k in range(3):
            renglon = "       "
            for i in range(3):
                id=self.convertirCoordenadasEnId([i,2,k])
                subCubo=self.SubCubos[id-1]
                color=subCubo.orientacionActual.obtenerColorEnCara(1)
                orientacion=Orientacion
                numero=orientacion.obtenerNumeroColor(orientacion,color)
                renglon=renglon+" "+str(numero)

            print(renglon)
        renglon=""
        for j in range(2,-1,-1):
            renglon = ""
            for k in range(3):
                id = self.convertirCoordenadasEnId([0, j, k])
                subCubo = self.SubCubos[id - 1]
                color = subCubo.orientacionActual.obtenerColorEnCara(2)
                orientacion = Orientacion
                numero = orientacion.obtenerNumeroColor(orientacion, color)
                renglon = renglon + " "+str(numero)

            agregar=" "
            for i in range(3):
                id = self.convertirCoordenadasEnId([0, j, k])
                subCubo = self.SubCubos[id - 1]
                color = subCubo.orientacionActual.obtenerColorEnCara(3)
                orientacion = Orientacion
                numero = orientacion.obtenerNumeroColor(orientacion, color)
                agregar = agregar + " " + str(numero)

            renglon=renglon+agregar
            agregar = " "
            for k in range(2,-1,-1):
                id = self.convertirCoordenadasEnId([2, j, k])
                subCubo = self.SubCubos[id - 1]
                color = subCubo.orientacionActual.obtenerColorEnCara(4)
                orientacion = Orientacion
                numero = orientacion.obtenerNumeroColor(orientacion, color)
                agregar = agregar + " "+str(numero)

            renglon = renglon + agregar
            agregar = " "
            for i in range(2, -1, -1):
                id = self.convertirCoordenadasEnId([i, j, 0])
                subCubo = self.SubCubos[id - 1]
                color = subCubo.orientacionActual.obtenerColorEnCara(5)
                orientacion = Orientacion
                numero = orientacion.obtenerNumeroColor(orientacion, color)
                agregar = agregar + " " + str(numero)
            print(renglon+agregar)

        for k in range(2,-1,-1):
            renglon = "       "
            for i in range(3):
                id = self.convertirCoordenadasEnId([i, 0, k])
                subCubo = self.SubCubos[id - 1]
                color = subCubo.orientacionActual.obtenerColorEnCara(6)
                orientacion = Orientacion
                numero = orientacion.obtenerNumeroColor(orientacion, color)
                renglon = renglon + " " + str(numero)
            print(renglon)



    def convertirCoordenadasEnId(self,coordenadas):
        return coordenadas[0]+3*coordenadas[1]+9*coordenadas[2]+1

    def convertirIdEnCoordenadas(self,id):
        cociente=math.floor((id-1)/3)
        x=(id-1)%3
        y=cociente%3
        z=math.floor(cociente/3)%3
        coordenadas=[x,y,z]
        return  coordenadas





