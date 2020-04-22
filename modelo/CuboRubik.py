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



                    if len(carasSubCubo==3):
                        coloresSubCubo = [colores[carasSubCubo[0] - 1], colores[carasSubCubo[1] - 1],
                                      colores[carasSubCubo[2] - 1]]
                        tipo="Esquina"
                    elif len(carasSubCubo==2):
                        coloresSubCubo = [colores[carasSubCubo[0] - 1], colores[carasSubCubo[1] - 1]]
                        tipo="Arista"
                    elif len(carasSubCubo==1):
                        tipo="Centro"
                        coloresSubCubo = [colores[carasSubCubo[0] - 1]]

                    posicionActual=Posicion(i,j,k)
                    posicionObjetivo=Posicion(i,j,k)


                    orientacionActual = Orientacion(carasSubCubo, coloresSubCubo)
                    orientacionObjetivo = Orientacion(carasSubCubo, coloresSubCubo)
                    subCubo = SubCubo(id, posicionActual, posicionObjetivo, orientacionActual, orientacionObjetivo,
                                      tipo)
                    self.SubCubos.append(subCubo)

