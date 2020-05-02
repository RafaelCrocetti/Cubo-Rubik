import math
import random as rnd
from modelo.SubCubo import SubCubo
from modelo.Manhattan import  Manhattan
#  representa el cubo como un conjunto de subcubos
# que se mueven dentro de una lista y que seon capaces de cambiar su orientacion
# y posicion
class CuboRubik:

    def __init__(self):
        # conjunto de subCubos que forman el cubo
        # se inicializa llenando la matriz de ceros
        self.SubCubos = [[[0 for i in range(3)] for j in range(3)] for k in range(3)]

        # conjunto de movientos validos del cubo
        self.movimientosValidos = ["F", "F'", "B", "B'", "U", "U'", "D", "D'", "L", "L'", "R", "R'"]
        id=0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    # esto ahorra las millones de lineas de codigo para
                    # verificar los 3 if, uno para cada coordenada

                    posicionActual=[i, j, k]

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
                    # 6: Azol
                    # 7: Sin Color
                    if id == 0:
                        orientacionActual=[2, 5, 6]
                    elif id==1:
                        orientacionActual=[5, 6]
                    elif id==2:
                        orientacionActual=[4, 5, 6]
                    elif id==3:
                        orientacionActual=[2, 5]
                    elif id==4:
                        orientacionActual=[5]
                    elif id==5:
                        orientacionActual=[4, 5]
                    elif id==6:
                        orientacionActual=[1, 2, 5]
                    elif id==7:
                        orientacionActual=[1, 5]
                    elif id==8:
                        orientacionActual=[1, 4, 5]
                    elif id==9:
                        orientacionActual=[2, 6]
                    elif id==10:
                        orientacionActual=[6]
                    elif id==11:
                        orientacionActual=[4, 6]
                    elif id==12:
                        orientacionActual=[2]
                    elif id==13:
                        orientacionActual=[7]
                    elif id==14:
                        orientacionActual=[4]
                    elif id==15:
                        orientacionActual=[1, 2]
                    elif id==16:
                        orientacionActual=[1]
                    elif id==17:
                        orientacionActual=[1, 4]
                    elif id==18:
                        orientacionActual=[2, 3, 6]
                    elif id==19:
                        orientacionActual=[3, 6]
                    elif id==20:
                        orientacionActual=[3, 4, 6]
                    elif id==21:
                        orientacionActual=[2, 3]
                    elif id==22:
                        orientacionActual=[3]
                    elif id==23:
                        orientacionActual=[3, 4]
                    elif id==24:
                        orientacionActual=[1, 2, 3]
                    elif id==25:
                        orientacionActual=[1, 3]
                    elif id==26:
                        orientacionActual=[1, 3, 4]
                    # este else solo existe para evitar un warning en el codigo
                    else:
                        orientacionActual=[7]

                    self.SubCubos[i][j][k]=SubCubo(posicionActual,posicionActual,orientacionActual,orientacionActual,orientacionActual)
                    id=id+1


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




    # convierte la posicion de un subCubo en la lista de subcubos a una lista de planos ocupados por los stikers del subcubo
    # para subcubos ubicados en las caras  frontal y trasera
    # se posiciona la vista en frente a la cara a rotar y ahi se hace la nomenclatura de plano con las siguientes
    # reglas:
    # 1- siempre se va en sentido horario
    # 2- siempre se termina en la cara a rotar
    # de la misma forma que el cubo los planos en un subCubo se encuentran enumerados
    # segun la siguiente nomenclatura
    # 0: posterior
    # 1: izquierda
    # 2: superior
    # 3: derecha
    # 4: inferior
    # 5: frontal
    # 6: ninguna
    def convertirPosicionLinealEnCoordenadasPlanosFrontal(self, lineal):

        if lineal == 0:
            # tiene tres planos con stikers porque es una esquina
            # el ultimo plano nombrado es el de la cara a rotar es decir 5
            planos = [4, 1, 5]
        elif lineal == 1:
            # tiene dos planos con stikers porque es una arista
            planos = [4, 5]
        elif lineal == 2:
            planos = [3, 4, 5]
        elif lineal == 6:
            planos = [1, 4, 0]
        elif lineal == 7:
            planos = [4, 0]
        elif lineal == 8:
            planos = [4, 3, 0]
        elif lineal == 9:
            planos = [1, 5]
        elif lineal == 10:
            planos = [5]
        elif lineal == 11:
            planos = [3, 5]

        elif lineal == 15:
            planos = [1, 0]
        elif lineal == 16:
            planos = [0]
        elif lineal == 17:
            planos = [3, 0]
        elif lineal == 18:
            planos = [1, 2, 5]
        elif lineal == 19:
            planos = [2, 5]
        elif lineal == 20:
            planos = [2, 3, 5]

        elif lineal == 24:
            planos = [2, 1, 0]
        elif lineal == 25:
            planos = [2, 0]
        elif lineal == 26:
            planos = [3, 2, 0]
        return planos
    # funciona igual que la funcion antarior pero para las caras Izquierda y Derecha
    def convertirPosicionLinealEnCoordenadasPlanosIzquierda(self, lineal):

        if lineal == 0:
            planos = [5,4,1]

        elif lineal == 2:
            planos = [ 4, 5, 3]
        elif lineal == 3:
            planos = [4, 1]

        elif lineal == 5:
            planos = [4, 3]
        elif lineal == 6:
            planos = [ 4, 0,1]

        elif lineal == 8:
            planos = [0, 4, 3]
        elif lineal == 9:
            planos = [5,1]

        elif lineal == 11:
            planos = [5, 3]
        elif lineal == 12:
            planos = [1]

        elif lineal == 14:
            planos = [3]
        elif lineal == 15:
            planos = [0, 1]

        elif lineal == 17:
            planos = [0, 3]
        elif lineal == 18:
            planos = [ 2, 5,1]

        elif lineal == 20:
            planos = [ 5, 2, 3]
        elif lineal == 21:
            planos = [2, 1]

        elif lineal == 23:
            planos = [2, 3]
        elif lineal == 24:
            planos = [0, 2, 1]

        elif lineal == 26:
            planos = [ 2, 0,3]
        return planos

    # funciona igual que la funcion antarior pero para las caras Superior e Inferior
    def convertirPosicionLinealEnCoordenadasPlanosSuperior(self, lineal):
        if lineal==0:
            planos=[1,5,4]
        elif lineal==1:
            planos=[5,4]
        elif lineal==2:
            planos=[5, 3, 4]
        elif lineal==3:
            planos=[1, 4]
        elif lineal==4:
            planos=[4]
        elif lineal==5:
            planos=[3, 4]
        elif lineal==6:
            planos=[0, 1, 4]
        elif lineal==7:
            planos=[0, 4]
        elif lineal==8:
            planos=[3, 0, 4]
        elif lineal==18:
            planos=[5, 1, 2]
        elif lineal==19:
            planos=[5, 2]
        elif lineal==20:
            planos=[3, 5, 2]
        elif lineal==21:
            planos=[1, 2]
        elif lineal==22:
            planos=[2]
        elif lineal==23:
            planos=[3, 2]
        elif lineal==24:
            planos=[1, 0, 2]
        elif lineal==25:
            planos=[0, 2]
        elif lineal==26:
            planos=[0, 3, 2]

        return planos

    # rota la cara frontal en sentido horario
    def rotarCaraFrontalHorario(self):

        self.rotarValoresFrontalesHorario([20,18,0,2])

        self.rotarValoresFrontalesHorario([19,9,1,11])

    # rota la cara frontal en sentido anti horario
    def rotarCaraFrontalAntiHorario(self):

        self.rotarValoresFrontalesHorario([2,0,18,20])

        self.rotarValoresFrontalesHorario([11,1,9,19])

    # rota la cara posterior en sentido horario
    def rotarCaraPosteriorHorario(self):

        # usa la misma funcion que frontal porque ambos
        # utilizan una topologia de planos similar
        self.rotarValoresFrontalesHorario([8,6,24,26])

        self.rotarValoresFrontalesHorario([17,7,15,25])

    # rota la cara posterior en sentido anti horario
    def rotarCaraPosteriorAntiHorario(self):
        self.rotarValoresFrontalesHorario([26,24,6,8])

        self.rotarValoresFrontalesHorario([25,15,7,17])

    # rota la cara izquierda en sentido horario
    def rotarCaraIzquierdaHorario(self):
        self.rotarValoresIzquierdaReloj([18, 24, 6, 0])
        self.rotarValoresIzquierdaReloj([21, 15, 3, 9])

    # rota la cara izquierda en sentido anti horario
    def rotarCaraIzquierdaAntiHorario(self):
        self.rotarValoresIzquierdaReloj([18, 0, 6, 24])
        self.rotarValoresIzquierdaReloj([21, 9, 3, 15])

    # rota la cara derecha en sentido horario
    def rotarCaraDerechaHorario(self):
        # usa la misma funcion que para izquierda porque
        # tienen un origen de coordenadas comun con esa
        # defincion de planos
        self.rotarValoresIzquierdaReloj([26,20,2,8])
        self.rotarValoresIzquierdaReloj([23,11,5,17])

    # rota la cara derecha en sentido anti horario
    def rotarCaraDerechaAntiHorario(self):
        self.rotarValoresIzquierdaReloj([26,8,2,20])
        self.rotarValoresIzquierdaReloj([23,17,5,11])

    # rota la cara superior en sentido horario
    def rotarCaraSuperiorHorario(self):
        self.rotarValoresSuperiorReloj([26, 24, 18, 20])
        self.rotarValoresSuperiorReloj([25, 21, 19, 23])

    # rota la cara superior en sentido anti horario
    def rotarCaraSuperiorAntiHorario(self):
        self.rotarValoresSuperiorReloj([26, 20, 18, 24])
        self.rotarValoresSuperiorReloj([25, 23, 19, 21])

    # rota la cara inferior en sentido horario
    def rotarCaraInferiorHorario(self):
        self.rotarValoresSuperiorReloj([8, 6, 0, 2])
        self.rotarValoresSuperiorReloj([7, 3, 1, 5])

    # rota la cara inferior en sentido anti horario
    def rotarCaraInferiorAntiHorario(self):
        self.rotarValoresSuperiorReloj([8, 2, 0, 6])
        self.rotarValoresSuperiorReloj([7, 5, 1, 3])

    # toma una lista de posiciones en la lista de subcubos e intercambia en el espacio
    # de posiciones cartesianas y de orientacion de los subcubos los elementos de la lista
    # siguiendo el siguiente orden el primer elemnto es sobreescrito por el segundo, el segundo por el tercero
    # etc
    def rotarValoresFrontalesHorario(self,valoresRotar):
        # cantidad de subcuboos a permutar
        cantidadValores=len(valoresRotar)

        # se crea una variable para almacenar la informacion del primer elemento
        subCuboAuxiliar=SubCubo(0,0,0,0,0)
        # se guarda una copia del primer elemento
        subCuboAuxiliar.copiarSubCubo(self.SubCubos[valoresRotar[0]])
        for i in range(0,cantidadValores-1,1):

            # posicion actual en la lista de subcubos a permutar
            valorActual=valoresRotar[i]
            # siguiente posicion en lista de subcubos a permutar
            siguienteValor=valoresRotar[i+1]

            # se transforma al subucubo actual en una copia del siguiente
            self.SubCubos[valorActual].copiarSubCubo(self.SubCubos[siguienteValor])
            # se corrije la posicion para que refleje la que ocupaba el subcubo actual
            # antes de ser sobre escrito por la del siguiente sub cubo
            self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)

            # lista de planos con colores en la orientacion del subcubo actual
            planosActual= self.convertirPosicionLinealEnCoordenadasPlanosFrontal(valorActual)
            # lista de planos con colores en la orientacion  del subcubo siguiente
            planosSiguiente= self.convertirPosicionLinealEnCoordenadasPlanosFrontal(siguienteValor)

            # borra los datos de la orientacion del subcubo actual ya que no solo estan desactualizadas
            # sino que podria generar errores si no se manda a cero
            self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
            for j in range(len(planosSiguiente)):
                # actualiza los valores de los colores en la orientacion actual para que se
                # matcheen con los del subocubo siguiente
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=self.SubCubos[siguienteValor].orientacionColoresActual[planosSiguiente[j]]


        # repite el proceso con el ultimo subcubo asociandole los datos del priemro que se
        # guardaron anteriormente
        valorActual=valoresRotar[len(valoresRotar)-1]
        siguienteValor=valoresRotar[0]
        self.SubCubos[valorActual].copiarSubCubo(subCuboAuxiliar)
        self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
        planosSiguiente = self.convertirPosicionLinealEnCoordenadasPlanosFrontal(siguienteValor)
        planosActual = self.convertirPosicionLinealEnCoordenadasPlanosFrontal(valorActual)
        self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
        for j in range(len(planosSiguiente)):
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=subCuboAuxiliar.orientacionColoresActual[planosSiguiente[j]]

    # actua de forma identica que el metodo anterior pero las definiciones de los
    # planos que consulta son distintas , es decir corresponden a otra funcion de matcheo del espacio de la recta
    # dentro del array de subcubos y un conjunto de 1 a 3 planos ordenados que indican las caras que este subcubo tiene
    # pintadas
    def rotarValoresIzquierdaReloj(self,valoresRotar):
        cantidadValores=len(valoresRotar)
        subCuboAuxiliar=SubCubo(0,0,0,0,0)
        subCuboAuxiliar.copiarSubCubo(self.SubCubos[valoresRotar[0]])
        for i in range(0,cantidadValores-1,1):
            valorActual=valoresRotar[i]
            siguienteValor=valoresRotar[i+1]

            self.SubCubos[valorActual].copiarSubCubo(self.SubCubos[siguienteValor])
            self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)

            planosSiguiente= self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(siguienteValor)
            planosActual= self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(valorActual)
            self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
            for j in range(len(planosSiguiente)):
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=self.SubCubos[siguienteValor].orientacionColoresActual[planosSiguiente[j]]
        valorActual=valoresRotar[len(valoresRotar)-1]
        siguienteValor=valoresRotar[0]
        self.SubCubos[valorActual].copiarSubCubo(subCuboAuxiliar)
        self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
        planosSiguiente = self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(siguienteValor)
        planosActual = self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(valorActual)
        self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
        for j in range(len(planosSiguiente)):
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=subCuboAuxiliar.orientacionColoresActual[planosSiguiente[j]]

    # lo mismo que la funcion anterior pero aplica a las caras Superior e Inferior
    def rotarValoresSuperiorReloj(self,valoresRotar):
        cantidadValores=len(valoresRotar)
        subCuboAuxiliar=SubCubo(0,0,0,0,0)
        subCuboAuxiliar.copiarSubCubo(self.SubCubos[valoresRotar[0]])
        for i in range(0,cantidadValores-1,1):
            valorActual=valoresRotar[i]
            siguienteValor=valoresRotar[i+1]

            self.SubCubos[valorActual].copiarSubCubo(self.SubCubos[siguienteValor])
            self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)

            planosSiguiente= self.convertirPosicionLinealEnCoordenadasPlanosSuperior(siguienteValor)
            planosActual= self.convertirPosicionLinealEnCoordenadasPlanosSuperior(valorActual)
            self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
            for j in range(len(planosSiguiente)):
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=self.SubCubos[siguienteValor].orientacionColoresActual[planosSiguiente[j]]
        valorActual=valoresRotar[len(valoresRotar)-1]
        siguienteValor=valoresRotar[0]
        self.SubCubos[valorActual].copiarSubCubo(subCuboAuxiliar)
        self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
        planosSiguiente = self.convertirPosicionLinealEnCoordenadasPlanosSuperior(siguienteValor)
        planosActual = self.convertirPosicionLinealEnCoordenadasPlanosSuperior(valorActual)
        self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
        for j in range(len(planosSiguiente)):
                self.SubCubos[valorActual].orientacionColoresActual[planosActual[j]]=subCuboAuxiliar.orientacionColoresActual[planosSiguiente[j]]

    # toma un string de movimientos separados por comas en la nomenclatura Singemaster
    #  y los ejecuta en el cubo
    def realizarMovimiento(self, movimiento):
        rotaciones = movimiento.split(",")
        for i in range(len(rotaciones)):
            if rotaciones[i] == "F":
                self.rotarCaraFrontalHorario()
            elif rotaciones[i] == "F'":
                self.rotarCaraFrontalAntiHorario()
            elif rotaciones[i] == "B":
                self.rotarCaraPosteriorHorario()
            elif rotaciones[i] == "B'":
                self.rotarCaraPosteriorAntiHorario()
            elif rotaciones[i] == "U":
                self.rotarCaraSuperiorHorario()
            elif rotaciones[i] == "U'":
                self.rotarCaraSuperiorHorario()
            elif rotaciones[i] == "D":
                self.rotarCaraInferiorHorario()
            elif rotaciones[i] == "D'":
                self.rotarCaraInferiorAntiHorario()
            elif rotaciones[i] == "L":
                self.rotarCaraIzquierdaHorario()
            elif rotaciones[i] == "L'":
                self.rotarCaraIzquierdaAntiHorario()
            elif rotaciones[i] == "R":
                self.rotarCaraDerechaHorario()
            elif rotaciones[i] == "R'":
                self.rotarCaraDerechaAntiHorario()

    # genera una secuencia al azar de movimientos para mezclar el cubo
    def generarSecuenciaMezclado(self, cantidadMovimientos):

        siguienteIndice = rnd.randint(0, 11)
        siguienteMovimiento = self.movimientosValidos[siguienteIndice]
        movimientos = siguienteMovimiento
        for i in range(cantidadMovimientos - 1):
            siguienteIndice = rnd.randint(0, 11)
            siguienteMovimiento = self.movimientosValidos[siguienteIndice]
            movimientos = movimientos + "," + siguienteMovimiento
        return movimientos

    # halla la distancia manhatam al cubo solucion
    def hallarDistancaSolucion(self):
        distancia = 0
        for i in range(len(self.SubCubos)):
            distancia = distancia + Manhattan.hallarDistanciaManhattan(self.SubCubos[i].posicionActual,self.SubCubos[i].posicionObjetivo)
        return distancia
    #halla la distancia manhatam entre a otro cubo
    def hallarDistanciaACubo(self,cubo):
        distancia=0
        for i in range(len(self.SubCubos)):
            distancia=distancia+Manhattan.hallarDistanciaManhattan(self.SubCubos[i].posicionActual,cubo.hallarSubCubo(self.SubCubos[i].id).posicionActual)
        return distancia

    # devuelve la referencia a un subCubo dado su id
    def hallarSubCubo(self,id):
        for i in range(len(self.SubCubos)):
            if self.SubCubos[i].id==id:
                return self.SubCubos[i]

    # verifica si cada uno de los subcubos se encuentra en su estado objetivo
    def esSolucion(self):
        for i in range(len(self.SubCubos)):
            if  not self.SubCubos[i].enEstadoObjetivo():
                return False
        return True

    # verifica si un cubo es igual a otro
    def esIgual(self,cubo):
        for i in range(len(self.SubCubos)):
            if not self.SubCubos[i].esIgual(cubo.SubCubos[i]):
                return False
        return  True

