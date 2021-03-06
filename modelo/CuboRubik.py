import random as rnd
import numpy as np
from modelo.Manhattan import Manhattan
from modelo.SubCubo import SubCubo


#  representa el cubo como un conjunto de subcubos
# que se mueven dentro de una lista y que seon capaces de cambiar su orientacion
# y posicion
class CuboRubik:

    def __init__(self):
        # conjunto de subCubos que forman el cubo
        # se inicializa llenando la matriz de ceros
        self.SubCubos = [[[0 for i in range(3)] for j in range(3)] for k in range(3)]

        id=0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    # esto ahorra las millones de lineas de codigo para
                    # verificar los 3 if, uno para cada coordenada

                    posicionActual=[i, j, k]
                    posicionObjetivo=[i, j, k]

                    # cada plano es representado por un numero de acuerdo a la siguiente nomclatura
                    # 1: posterior
                    # 2: izquierda
                    # 3: superior
                    # 4: derecha
                    # 5: inferior
                    # 6: frontal
                    # 7: ninguna
                    # cada color es representado por un numero de acuerdo a  la siguiente nomclatura
                    # 1: Verde
                    # 2: Amarillo
                    # 3: Rojo
                    # 4: Blanco
                    # 5: Naranja
                    # 6: Azul
                    # 7: Sin Color
                    if id == 0:
                        orientacionActual=[2, 5, 6]
                        orientacionObjetivo=[2, 5, 6]
                        colores=[2, 5, 6]
                    elif id==1:
                        orientacionActual=[5, 6]
                        orientacionObjetivo=[5, 6]
                        colores=[5, 6]
                    elif id==2:
                        orientacionActual=[4, 5, 6]
                        orientacionObjetivo=[4, 5, 6]
                        colores=[4, 5, 6]
                    elif id==3:
                        orientacionActual=[2, 5]
                        orientacionObjetivo=[2, 5]
                        colores=[2, 5]
                    elif id==4:
                        orientacionActual=[5]
                        orientacionObjetivo=[5]
                        colores=[5]
                    elif id==5:
                        orientacionActual=[4, 5]
                        orientacionObjetivo=[4, 5]
                        colores=[4, 5]
                    elif id==6:
                        orientacionActual=[1, 2, 5]
                        orientacionObjetivo=[1, 2, 5]
                        colores=[1, 2, 5]
                    elif id==7:
                        orientacionActual=[1, 5]
                        orientacionObjetivo=[1, 5]
                        colores=[1, 5]
                    elif id==8:
                        orientacionActual=[1, 4, 5]
                        orientacionObjetivo=[1, 4, 5]
                        colores=[1, 4, 5]
                    elif id==9:
                        orientacionActual=[2, 6]
                        orientacionObjetivo=[2, 6]
                        colores=[2, 6]
                    elif id==10:
                        orientacionActual=[6]
                        orientacionObjetivo=[6]
                        colores=[6]
                    elif id==11:
                        orientacionActual=[4, 6]
                        orientacionObjetivo=[4, 6]
                        colores=[4, 6]
                    elif id==12:
                        orientacionActual=[2]
                        orientacionObjetivo=[2]
                        colores=[2]
                    elif id==13:
                        orientacionActual=[7]
                        orientacionObjetivo=[7]
                        colores=[7]
                    elif id==14:
                        orientacionActual=[4]
                        orientacionObjetivo=[4]
                        colores=[4]
                    elif id==15:
                        orientacionActual=[1, 2]
                        orientacionObjetivo=[1, 2]
                        colores=[1, 2]
                    elif id==16:
                        orientacionActual=[1]
                        orientacionObjetivo=[1]
                        colores=[1]
                    elif id==17:
                        orientacionActual=[1, 4]
                        orientacionObjetivo=[1, 4]
                        colores=[1, 4]
                    elif id==18:
                        orientacionActual=[2, 3, 6]
                        orientacionObjetivo=[2, 3, 6]
                        colores=[2, 3, 6]
                    elif id==19:
                        orientacionActual=[3, 6]
                        orientacionObjetivo=[3, 6]
                        colores=[3, 6]
                    elif id==20:
                        orientacionActual=[3, 4, 6]
                        orientacionObjetivo=[3, 4, 6]
                        colores=[3, 4, 6]
                    elif id==21:
                        orientacionActual=[2, 3]
                        orientacionObjetivo=[2, 3]
                        colores=[2, 3]
                    elif id==22:
                        orientacionActual=[3]
                        orientacionObjetivo=[3]
                        colores=[3]
                    elif id==23:
                        orientacionActual=[3, 4]
                        orientacionObjetivo=[3, 4]
                        colores=[3, 4]
                    elif id==24:
                        orientacionActual=[1, 2, 3]
                        orientacionObjetivo=[1, 2, 3]
                        colores=[1, 2, 3]
                    elif id==25:
                        orientacionActual=[1, 3]
                        orientacionObjetivo=[1, 3]
                        colores=[1, 3]
                    elif id==26:
                        orientacionActual=[1, 3, 4]
                        orientacionObjetivo=[1, 3, 4]
                        colores=[1, 3, 4]
                    # este else solo existe para evitar un warning en el codigo
                    else:
                        orientacionActual=[7]
                        orientacionObjetivo=[7]
                        colores=[7]

                    self.SubCubos[i][j][k]=SubCubo(posicionActual,posicionObjetivo,colores,orientacionActual,orientacionObjetivo)
                    id=id+1


    # conjunto de movientos validos del cubo
    @staticmethod
    def movimientosValidos():
        return ["F", "F'", "F2", "B", "B'", "B2", "U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2"];
    # muestra  en plantalla el cubo desarrollado de acuerdo al siguiente orden
    # 1: posterior
    # 2: izquierda
    # 3: superior
    # 4: derecha
    # 5: inferior
    # 6: frontal
    # 7: ninguna
    # cada color es representado por un numero siguiendo la siguiente nomclatura
    # 1: Verde
    # 2: Amarillo
    # 3: Rojo
    # 4: Blanco
    # 5: Naranja
    # 6: Azol
    # 7: Sin Color

    def print(self):

        #cara 1
        for k in range(3):
            renglon = "       "
            for i in range(3):
                subCubo=self.SubCubos[i][2][k]
                color=subCubo.obtenerColorPlano(1)

                renglon=renglon+" "+str(color)

            print(renglon)

        for j in range(2,-1,-1):
            renglon = ""
            # cara 2
            for k in range(3):
                subCubo=self.SubCubos[0][ j][ k]
                color=subCubo.obtenerColorPlano(2)
                renglon = renglon + " "+str(color)
            # cara 3
            agregar=" "
            for i in range(3):
                subCubo=self.SubCubos[i][j][2]
                color=subCubo.obtenerColorPlano(3)
                agregar = agregar + " " + str(color)

            renglon=renglon+agregar
            agregar = " "
            #cara 4
            for k in range(2,-1,-1):
                subCubo=self.SubCubos[2][j][k]
                color=subCubo.obtenerColorPlano(4)
                agregar = agregar + " "+str(color)

            renglon = renglon + agregar
            agregar = " "
            #cara 5
            for i in range(2,-1,-1):
                subCubo=self.SubCubos[i][j][0]
                color=subCubo.obtenerColorPlano(5)
                agregar = agregar + " " + str(color)
            renglon = renglon + agregar
            print(renglon)

        #cara 6
        for k in range(2,-1,-1):
            renglon = "       "
            for i in range(3):
                subCubo=self.SubCubos[i][0][k]
                color=subCubo.obtenerColorPlano(6)
                renglon = renglon + " " + str(color)
            print(renglon)




    # rota la cara frontal en sentido horario
    def rotarCaraFrontalHorario(self):

        self.rotarValoresHorario([20,18,0,2])

        self.rotarValoresHorario([19,9,1,11])

        for k in range(3):
            for i in range(3):
                subCubo = self.SubCubos[i][0][k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 6:
                        if subCubo.orientacionActual[l] != 5:
                            subCubo.orientacionActual[l] = subCubo.orientacionActual[l] + 1
                        else:
                            subCubo.orientacionActual[l] = 2


    # rota la cara frontal en sentido anti horario
    def rotarCaraFrontalAntiHorario(self):

        self.rotarValoresHorario([2,0,18,20])

        self.rotarValoresHorario([11,1,9,19])
        for k in range(3):
            for i in range(3):
                subCubo = self.SubCubos[i][0][k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 6:
                        if subCubo.orientacionActual[l] != 2:
                            subCubo.orientacionActual[l] = subCubo.orientacionActual[l] -1
                        else:
                            subCubo.orientacionActual[l] = 5

    # rota la cara posterior en sentido horario
    def rotarCaraPosteriorHorario(self):

        self.rotarValoresHorario([8,6,24,26])

        self.rotarValoresHorario([17,7,15,25])
        for k in range(3):
            for i in range(3):
                subCubo = self.SubCubos[i][2][k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 1:
                        if subCubo.orientacionActual[l] != 2:
                            subCubo.orientacionActual[l] = subCubo.orientacionActual[l] -1
                        else:
                            subCubo.orientacionActual[l] = 5

    # rota la cara posterior en sentido anti horario
    def rotarCaraPosteriorAntiHorario(self):
        self.rotarValoresHorario([26,24,6,8])

        self.rotarValoresHorario([25,15,7,17])


        for k in range(3):
            for i in range(3):
                subCubo = self.SubCubos[i][2][k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 1:
                        if subCubo.orientacionActual[l] != 5:
                            subCubo.orientacionActual[l] = subCubo.orientacionActual[l] +1
                        else:
                            subCubo.orientacionActual[l] = 2

    # rota la cara izquierda en sentido horario
    def rotarCaraIzquierdaHorario(self):
        self.rotarValoresHorario([18, 24, 6, 0])
        self.rotarValoresHorario([21, 15, 3, 9])
        for j in range(3):
            for k in range(3):
                subCubo=self.SubCubos[0][ j][ k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 2:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =3
                        elif subCubo.orientacionActual[l] == 3:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 5
                        elif subCubo.orientacionActual[l] == 5:
                            subCubo.orientacionActual[l] = 1


    # rota la cara izquierda en sentido anti horario
    def rotarCaraIzquierdaAntiHorario(self):
        self.rotarValoresHorario([18, 0, 6, 24])
        self.rotarValoresHorario([21, 9, 3, 15])
        for j in range(3):
            for k in range(3):
                subCubo=self.SubCubos[0][ j][ k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 2:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =5
                        elif subCubo.orientacionActual[l] == 3:
                            subCubo.orientacionActual[l] = 1
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 3
                        elif subCubo.orientacionActual[l] == 5:
                            subCubo.orientacionActual[l] = 6

    # rota la cara derecha en sentido horario
    # PENDIENTE: implementar esta rotacion
    def rotarCaraDerechaHorario(self):
        # usa la misma funcion que para izquierda porque
        # tienen un origen de coordenadas comun con esa
        # defincion de planos
        self.rotarValoresHorario([26,20,2,8])
        self.rotarValoresHorario([23,11,5,17])
        for j in range(3):
            for k in range(3):
                subCubo=self.SubCubos[2][ j][ k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 4:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =5
                        elif subCubo.orientacionActual[l] == 3:
                            subCubo.orientacionActual[l] = 1
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 3
                        elif subCubo.orientacionActual[l] == 5:
                            subCubo.orientacionActual[l] = 6

    # rota la cara derecha en sentido anti horario
    def rotarCaraDerechaAntiHorario(self):
        self.rotarValoresHorario([26,8,2,20])
        self.rotarValoresHorario([23,17,5,11])
        for j in range(3):
            for k in range(3):
                subCubo=self.SubCubos[2][ j][ k]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 4:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =3
                        elif subCubo.orientacionActual[l] == 3:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 5
                        elif subCubo.orientacionActual[l] == 5:
                            subCubo.orientacionActual[l] = 1

    # rota la cara superior en sentido horario
    def rotarCaraSuperiorHorario(self):
        self.rotarValoresHorario([26, 24, 18, 20])
        self.rotarValoresHorario([25, 21, 19, 23])
        for j in range(3):
            for i in range(3):
                subCubo=self.SubCubos[i][j][2]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 3:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =4
                        elif subCubo.orientacionActual[l] == 4:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 2
                        elif subCubo.orientacionActual[l] == 2:
                            subCubo.orientacionActual[l] = 1

    # rota la cara superior en sentido anti horario
    def rotarCaraSuperiorAntiHorario(self):
        self.rotarValoresHorario([26, 20, 18, 24])
        self.rotarValoresHorario([25, 23, 19, 21])
        for j in range(3):
            for i in range(3):
                subCubo=self.SubCubos[i][j][2]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 3:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =2
                        elif subCubo.orientacionActual[l] == 2:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 4
                        elif subCubo.orientacionActual[l] == 4:
                            subCubo.orientacionActual[l] = 1

    # rota la cara inferior en sentido horario
    def rotarCaraInferiorHorario(self):
        self.rotarValoresHorario([6, 8, 2, 0])
        self.rotarValoresHorario([7, 5, 1, 3])
        for j in range(3):
            for i in range(3):
                subCubo=self.SubCubos[i][j][0]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 5:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] =2
                        elif subCubo.orientacionActual[l] == 2:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 4
                        elif subCubo.orientacionActual[l] == 4:
                            subCubo.orientacionActual[l] = 1

    # rota la cara inferior en sentido anti horario
    # PENDIENTE: implementar esta rotacion
    def rotarCaraInferiorAntiHorario(self):
        self.rotarValoresHorario([6, 0, 2, 8])
        self.rotarValoresHorario([7, 3, 1, 5])
        for j in range(3):
            for i in range(3):
                subCubo = self.SubCubos[i][j][0]
                for l in range(len(subCubo.orientacionActual)):
                    if subCubo.orientacionActual[l] != 5:
                        if subCubo.orientacionActual[l] == 1:
                            subCubo.orientacionActual[l] = 4
                        elif subCubo.orientacionActual[l] == 4:
                            subCubo.orientacionActual[l] = 6
                        elif subCubo.orientacionActual[l] == 6:
                            subCubo.orientacionActual[l] = 2
                        elif subCubo.orientacionActual[l] == 2:
                            subCubo.orientacionActual[l] = 1

    # toma una lista de ids e intercambia en el espacio
    # de posiciones cartesianas los elementos de la lista
    # siguiendo el siguiente orden el primer elemnto es sobreescrito por el segundo, el segundo por el tercero
    # etc
    def rotarValoresHorario(self,valoresRotar):
        # cantidad de subcuboos a permutar
        cantidadValores=len(valoresRotar)

        # se crea una variable para almacenar la informacion del primer elemento
        subCuboAuxiliar=SubCubo([0, 0, 0],[0, 0, 0],0,0,0)

        # se guarda una copia del primer elemento
        subCuboAuxiliar.copiarSubCubo(self.obtenerSubCuboEnPosicion(SubCubo.convertirIdEnCoordenadas(valoresRotar[0])))
        for i in range(0,cantidadValores-1,1):

            # posicion actual en la lista de subcubos a permutar
            posicionActual=SubCubo.convertirIdEnCoordenadas(valoresRotar[i])
            # siguiente posicion en lista de subcubos a permutar
            posicionSiguiente=SubCubo.convertirIdEnCoordenadas(valoresRotar[i+1])

            # se transforma al subucubo actual en una copia del siguiente
            self.obtenerSubCuboEnPosicion(posicionActual).copiarSubCubo(self.obtenerSubCuboEnPosicion(posicionSiguiente))
            # se corrije la posicion para que refleje la que ocupaba el subcubo actual
            # antes de ser sobre escrito por la del siguiente sub cubo
            self.obtenerSubCuboEnPosicion(posicionActual).posicionActual=posicionActual


        # repite el proceso con el ultimo subcubo asociandole los datos del priemro que se
        # guardaron anteriormente
        posicionActual=SubCubo.convertirIdEnCoordenadas(valoresRotar[len(valoresRotar)-1])
        self.obtenerSubCuboEnPosicion(posicionActual).copiarSubCubo(subCuboAuxiliar)
        self.obtenerSubCuboEnPosicion(posicionActual).posicionActual=posicionActual


    # devuelve la referencia a un subCubo dado un vector de posicion
    # simplificando la sintaxis de algunas operaciones
    def obtenerSubCuboEnPosicion(self,posicion):
        return self.SubCubos[posicion[0]][posicion[1]][posicion[2]]

    # toma un string de movimientos separados por comas en la nomenclatura Singemaster
    #  y los ejecuta en el cubo
    def realizarMovimiento(self, movimiento):
        rotaciones = movimiento.split(" ")
        self.realizarMovimientoLista(rotaciones)

    def realizarMovimientoLista(self,rotaciones):
        for i in range(len(rotaciones)):
            if rotaciones[i] == "F":
                self.rotarCaraFrontalHorario()
            elif rotaciones[i] == "F'":
                self.rotarCaraFrontalAntiHorario()
            elif rotaciones[i] == "F2":
                self.rotarCaraFrontalHorario()
                self.rotarCaraFrontalHorario()
            elif rotaciones[i] == "B":
                self.rotarCaraPosteriorHorario()
            elif rotaciones[i] == "B'":
                self.rotarCaraPosteriorAntiHorario()
            elif rotaciones[i] == "B2":
                self.rotarCaraPosteriorHorario()
                self.rotarCaraPosteriorHorario()
            elif rotaciones[i] == "U":
                self.rotarCaraSuperiorHorario()
            elif rotaciones[i] == "U'":
                self.rotarCaraSuperiorHorario()
            elif rotaciones[i] == "U2":
                self.rotarCaraSuperiorHorario()
                self.rotarCaraSuperiorHorario()
            elif rotaciones[i] == "D":
                self.rotarCaraInferiorHorario()
            elif rotaciones[i] == "D'":
                self.rotarCaraInferiorAntiHorario()
            elif rotaciones[i] == "D2":
                self.rotarCaraInferiorHorario()
                self.rotarCaraInferiorHorario()
            elif rotaciones[i] == "L":
                self.rotarCaraIzquierdaHorario()
            elif rotaciones[i] == "L'":
                self.rotarCaraIzquierdaAntiHorario()
            elif rotaciones[i] == "L2":
                self.rotarCaraIzquierdaHorario()
                self.rotarCaraIzquierdaHorario()
            elif rotaciones[i] == "R":
                self.rotarCaraDerechaHorario()
            elif rotaciones[i] == "R'":
                self.rotarCaraDerechaAntiHorario()
            elif rotaciones[i] == "R2":
                self.rotarCaraDerechaHorario()
                self.rotarCaraDerechaHorario()

    # genera una secuencia al azar de movimientos para mezclar el cubo
    @staticmethod
    def generarSecuenciaMezclado(cantidadMovimientos):

        siguienteIndice = rnd.randint(0, 17)
        siguienteMovimiento = CuboRubik.movimientosValidos()[siguienteIndice]
        movimientos = siguienteMovimiento
        for i in range(cantidadMovimientos - 1):
            siguienteIndice = rnd.randint(0, 17)
            siguienteMovimiento = CuboRubik.movimientosValidos()[siguienteIndice]
            movimientos = movimientos + " " + siguienteMovimiento
        return movimientos

    # halla la distancia manhatam al cubo solucion
    def hallarDistancaSolucion(self):
        distancia = 0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    distancia = distancia + Manhattan.hallarDistanciaManhattan(self.SubCubos[i][j][k].posicionActual,self.SubCubos[i][j][k].posicionObjetivo)
        return distancia
    # halla la distancia manhatam a otro cubo
    def hallarDistanciaACubo(self,cubo):
        distancia=0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    distancia=distancia+Manhattan.hallarDistanciaManhattan(self.SubCubos[i][j][k].posicionActual,cubo.hallarSubCubo(self.SubCubos[i][j][k].id).posicionActual)
        return distancia

    # devuelve la referencia a un subCubo dado su id
    def hallarSubCubo(self,id):
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if self.SubCubos[i][j][k].id==id:
                        return self.SubCubos[i][j][k]

    # verifica si cada uno de los subcubos se encuentra en su estado objetivo
    def esSolucion(self):
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if not self.SubCubos[i][j][k].enEstadoObjetivo():
                        return False
        return True

    # verifica si un cubo es igual a otro
    def esIgual(self,cubo):
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if not self.SubCubos[i][j][k].esIgual(cubo.SubCubos[i][j][k]):
                        return False
        return  True
    @staticmethod
    def generarCubosMezclados(cantidadCubos,maximaCantidadMovimientos):
        cubosMezclados=[]
        cantidadMovimientos=np.random.normal(1.0, 0.005, cantidadCubos)
        print(cantidadMovimientos)
        for i in range(cantidadCubos):
            cubo=CuboRubik()
            cubo.realizarMovimiento(CuboRubik.generarSecuenciaMezclado(round(cantidadMovimientos[i]*maximaCantidadMovimientos)))
            cubosMezclados.append(cubo)
        return cubosMezclados
    def toOneHot(self):

        oneHotEncoding=[]
        # cara 1
        for k in range(3):
            renglon = "       "
            for i in range(3):
                subCubo = self.SubCubos[i][2][k]
                color = subCubo.obtenerColorPlano(1)
                self.pushColor(oneHotEncoding,color)


        for j in range(2, -1, -1):
            renglon = ""
            # cara 2
            for k in range(3):
                subCubo = self.SubCubos[0][j][k]
                color = subCubo.obtenerColorPlano(2)
                self.pushColor(oneHotEncoding,color)
            for i in range(3):
                subCubo = self.SubCubos[i][j][2]
                color = subCubo.obtenerColorPlano(3)
                self.pushColor(oneHotEncoding,color)
            # cara 4
            for k in range(2, -1, -1):
                subCubo = self.SubCubos[2][j][k]
                color = subCubo.obtenerColorPlano(4)
                self.pushColor(oneHotEncoding,color)
            # cara 5
            for i in range(2, -1, -1):
                subCubo = self.SubCubos[i][j][0]
                color = subCubo.obtenerColorPlano(5)
                self.pushColor(oneHotEncoding,color)

        # cara 6
        for k in range(2, -1, -1):
            renglon = "       "
            for i in range(3):
                subCubo = self.SubCubos[i][0][k]
                color = subCubo.obtenerColorPlano(6)
                self.pushColor(oneHotEncoding,color)
        return  oneHotEncoding
    def pushColor(self,array,color):
        if color==1:
            array.append(1)
            for i in range(5):
                array.append(0)
        elif color==2:
            for i in range(1):
                array.append(0)
            array.append(1)
            for i in range(4):
                array.append(0)
        elif color==3:
            for i in range(2):
                array.append(0)
            array.append(1)
            for i in range(3):
                array.append(0)
        elif color==4:
            for i in range(3):
                array.append(0)
            array.append(1)
            for i in range(2):
                array.append(0)
        elif color==5:
            for i in range(4):
                array.append(0)
            array.append(1)
            for i in range(1):
                array.append(0)
        else:
            for i in range(5):
                array.append(0)
            array.append(1)


