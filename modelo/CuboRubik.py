import math
from modelo.SubCubo import SubCubo
class CuboRubik:
    # PENDIENTE: documentar que puta es lo que hice aca
    def __init__(self):
        self.SubCubos=[]

        # se adapta la codificacion para las caras:
        # 0: posterior
        # 1: izquierda
        # 2: superior
        # 3: derecha
        # 4: inferior
        # 5: frontal
        # 6: ninguna
        # las caras estan enumeradas como un cubo desarrollado en un plano
        # y sus correspondiente colores abajo se calculan 
        # como igual al numero de cara y dara el indice correcto en este vector
        # para la posicionObjetivo
        # la idea es llenar la lista de subcubos con filas que lenen un
        # plano con tres filas y el cubo con tres planos
        # colores=["Verde","Amarillo","Rojo","Blanco","Naranja","Azul","Sin Color"]
        # coloresEnNumeros=[1,2,3,4,5,6,7]
        id=0
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if id==0:
                        orientacionActual = [0,2,0,0,5,6]
                        orientacionObjetivo = [0,2,0,0,5,6]
                    elif id==1:
                        orientacionActual = [0,0,0,0,5,6]
                        orientacionObjetivo = [0,0,0,0,5,6]
                    elif id==2:
                        orientacionActual = [0,0,0,4,5,6]
                        orientacionObjetivo = [0,0,0,4,5,6]
                    elif id==3:
                        orientacionActual = [0,2,0,0,5,0]
                        orientacionObjetivo = [0,2,0,0,5,0]
                    elif id==4:
                        orientacionActual = [0,0,0,0,5,0]
                        orientacionObjetivo = [0,0,0,0,5,0]
                    elif id==5:
                        orientacionActual = [0,0,0,4,5,0]
                        orientacionObjetivo = [0,0,0,4,5,0]
                    elif id==6:
                        orientacionActual = [1,2,0,0,5,0]
                        orientacionObjetivo = [1,2,0,0,5,0]
                    elif id==7:
                        orientacionActual = [1,0,0,0,5,0]
                        orientacionObjetivo = [1,0,0,0,5,0]
                    elif id==8:
                        orientacionActual = [1,0,0,4,5,0]
                        orientacionObjetivo = [1,0,0,4,5,0]
                    elif id==9:
                        orientacionActual = [0,2,0,0,0,6]
                        orientacionObjetivo = [0,2,0,0,0,6]
                    elif id==10:
                        orientacionActual = [0,0,0,0,0,6]
                        orientacionObjetivo = [0,0,0,0,0,6]
                    elif id==11:
                        orientacionActual = [0,0,0,4,0,6]
                        orientacionObjetivo = [0,0,0,4,0,6]
                    elif id==12:
                        orientacionActual = [0,2,0,0,0,0]
                        orientacionObjetivo = [0,2,0,0,0,0]
                    elif id==13:
                        orientacionActual = [0,0,0,0,0,0]
                        orientacionObjetivo = [0,0,0,0,0,0]
                    elif id==14:
                        orientacionActual = [0,0,0,4,0,0]
                        orientacionObjetivo = [0,0,0,4,0,0]
                    elif id==15:
                        orientacionActual = [1,2,0,0,0,0]
                        orientacionObjetivo = [1,2,0,0,0,0]
                    elif id==16:
                        orientacionActual = [1,0,0,0,0,0]
                        orientacionObjetivo = [1,0,0,0,0,0]
                    elif id==17:
                        orientacionActual = [1,0,0,4,0,0]
                        orientacionObjetivo = [1,0,0,4,0,0]
                    elif id==18:
                        orientacionActual   = [0,2,3,0,0,6]
                        orientacionObjetivo = [0,2,3,0,0,6]
                    elif id==19:
                        orientacionActual   = [0,0,3,0,0,6]
                        orientacionObjetivo = [0,0,3,0,0,6]
                    elif id==20:
                        orientacionActual   = [0,0,3,4,0,6]
                        orientacionObjetivo = [0,0,3,4,0,6]
                    elif id==21:
                        orientacionActual   = [0,2,3,0,0,0]
                        orientacionObjetivo = [0,2,3,0,0,0]
                    elif id==22:
                        orientacionActual   = [0,0,3,0,0,0]
                        orientacionObjetivo = [0,0,3,0,0,0]
                    elif id==23:
                        orientacionActual   = [0,0,3,4,0,0]
                        orientacionObjetivo = [0,0,3,4,0,0]
                    elif id==24:
                        orientacionActual   = [1,2,3,0,0,0]
                        orientacionObjetivo = [1,2,3,0,0,0]
                    elif id==25:
                        orientacionActual   = [1,0,3,0,0,0]
                        orientacionObjetivo = [1,0,3,0,0,0]
                    elif id==26:
                        orientacionActual   = [1,0,3,4,0,0]
                        orientacionObjetivo = [1,0,3,4,0,0]

                    posicionActual=[i,j,k]
                    posicionObjetivo=[i,j,k]


                    subCubo = SubCubo(id, posicionActual, posicionObjetivo, orientacionActual, orientacionObjetivo)
                    self.SubCubos.append(subCubo)
                    id=id+1

    def print(self):

        #cara 0
        for k in range(3):
            renglon = "       "
            for i in range(3):
                id=self.convertirCoordenadasEnPosicionLineal([i,2,k])
                subCubo=self.SubCubos[id]
                orientacion=subCubo.orientacionColoresActual
                color=subCubo.orientacionColoresActual[0]

                renglon=renglon+" "+str(color)

            print(renglon)

        for j in range(2,-1,-1):
            renglon = ""
            # cara 1
            for k in range(3):
                id = self.convertirCoordenadasEnPosicionLineal([0, j, k])
                subCubo=self.SubCubos[id]
                color=subCubo.orientacionColoresActual[1]
                renglon = renglon + " "+str(color)
            # cara 2
            agregar=" "
            for i in range(3):
                id = self.convertirCoordenadasEnPosicionLineal([i, j, 2])
                subCubo=self.SubCubos[id]
                color=subCubo.orientacionColoresActual[2]
                agregar = agregar + " " + str(color)

            renglon=renglon+agregar
            agregar = " "
            #cara 3
            for k in range(2,-1,-1):
                id = self.convertirCoordenadasEnPosicionLineal([2, j, k])
                subCubo=self.SubCubos[id]
                color=subCubo.orientacionColoresActual[3]
                agregar = agregar + " "+str(color)

            renglon = renglon + agregar
            agregar = " "
            #cara 4
            for i in range(2,-1,-1):
                id = self.convertirCoordenadasEnPosicionLineal([i, j, 0])
                subCubo=self.SubCubos[id]
                color=subCubo.orientacionColoresActual[4]
                agregar = agregar + " " + str(color)
            renglon = renglon + agregar
            print(renglon)

        #cara 5
        for k in range(2,-1,-1):
            renglon = "       "
            for i in range(3):
                id = self.convertirCoordenadasEnPosicionLineal([i, 0, k])
                subCubo=self.SubCubos[id]
                color=subCubo.orientacionColoresActual[5]
                renglon = renglon + " " + str(color)
            print(renglon)


    # convierte las coordenadas de un SyubCubo en la posicion en la lista de subCubos que le corresponde
    def convertirCoordenadasEnPosicionLineal(self,coordenadas):
        return coordenadas[0]+3*coordenadas[1]+9*coordenadas[2]

    # convierte la posicion de un subCubo en la lista a la posicion en el espacio que le corresponde
    def convertirPosicionLinealEnCoordenadas(self,lineal):
        cociente=math.floor((lineal)/3)
        x=(lineal)%3
        y=cociente%3
        z=math.floor(cociente/3)%3
        coordenadas=[x,y,z]
        return  coordenadas

    def convertirPosicionLinealEnCoordenadasPlanosFrontal(self, lineal):

        if lineal == 0:
            planos = [4, 1, 5]
        elif lineal == 1:
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
    # convierte la posicion de un subCubo en la lista a la posicion de los N planos que le corresponden
    # a esa posicion
    #PENDIENTE: revisar el orden de los planos, debe ser universal
    # esto funciono perfecto para las frontales y posteriores
    # PENDIENTE: averiguar por que?
    def convertirPosicionLinealEnCoordenadasPlanos(self,lineal):
        
        if lineal == 0:
            planos = [ 4, 1 ,5]
        elif lineal == 1:
            planos=[4, 5]
        elif lineal == 2:
            planos = [3, 4, 5]
        elif lineal == 3:
            planos =[4,1]
        elif lineal == 4:
            planos =[4]
        elif lineal == 5:
            planos =[4,3]
        elif lineal == 6:
            planos =[1,4,0]
        elif lineal == 7:
            planos =[4,0]
        elif lineal == 8:
            planos =[4,3,0]
        elif lineal == 9:
            planos =[1,5]
        elif lineal == 10:
            planos =[5]
        elif lineal == 11:
            planos =[3,5]
        elif lineal == 12:
            planos =[1]
        elif lineal == 13:
            planos =[6]
        elif lineal == 14:
            planos =[3]
        elif lineal == 15:
            planos =[1,0]
        elif lineal == 16:
            planos =[0]
        elif lineal == 17:
            planos =[3,0]
        elif lineal == 18:
            planos =[1,2,5]
        elif lineal == 19:
            planos =[2,5]
        elif lineal == 20:
            planos =[2,3,5]
        elif lineal == 21:
            planos =[2,1]
        elif lineal == 22:
            planos =[2]
        elif lineal == 23:
            planos =[2,3]
        elif lineal == 24:
            planos =[2,1,0]
        elif lineal == 25:
            planos =[2,0]
        elif lineal == 26:
            planos =[3,2,0]
        return planos
    def rotarCaraFrontalHorario(self):

        self.rotarValoresFrontalesReloj([20,18,0,2])

        self.rotarValoresFrontalesReloj([19,9,1,11])

    def rotarCaraFrontalAntiHorario(self):

        self.rotarValoresFrontalesReloj([2,0,18,20])

        self.rotarValoresFrontalesReloj([11,1,9,19])

    def rotarCaraPosteriorHorario(self):
        self.rotarValoresFrontalesReloj([8,6,24,26])

        self.rotarValoresFrontalesReloj([17,7,15,25])

    def rotarCaraPosteriorAntiHorario(self):
        self.rotarValoresFrontalesReloj([26,24,6,8])

        self.rotarValoresFrontalesReloj([25,15,7,17])

    def rotarCaraIzquierdaHorario(self):
        self.rotarValoresIzquierdaReloj([18, 24, 6, 0])
        self.rotarValoresIzquierdaReloj([21, 15, 3, 9])

    def rotarCaraIzquierdaAntiHorario(self):
        self.rotarValoresIzquierdaReloj([18, 0, 6, 24])
        self.rotarValoresIzquierdaReloj([21, 9, 3, 15])

    def rotarCaraDerechaHorario(self):
        self.rotarValoresIzquierdaReloj([26,20,2,8])
        self.rotarValoresIzquierdaReloj([23,11,5,17])

    def rotarCaraDerechaAntiHorario(self):
        self.rotarValoresIzquierdaReloj([26,8,2,20])
        self.rotarValoresIzquierdaReloj([23,17,5,11])

    def rotarValoresFrontalesReloj(self,valoresRotar):
        cantidadValores=len(valoresRotar)
        subCuboAuxiliar=SubCubo(0,0,0,0,0)
        subCuboAuxiliar.copiarSubCubo(self.SubCubos[valoresRotar[0]])
        for i in range(0,cantidadValores-1,1):
            valorActual=valoresRotar[i]
            siguienteValor=valoresRotar[i+1]

            self.SubCubos[valorActual].copiarSubCubo(self.SubCubos[siguienteValor])
            posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
            self.SubCubos[valorActual].posicionActual=posicionActual

            planosSiguiente= self.convertirPosicionLinealEnCoordenadasPlanosFrontal(siguienteValor)
            planosActual= self.convertirPosicionLinealEnCoordenadasPlanosFrontal(valorActual)
            self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
            for j in range(len(planosSiguiente)):
                planoParaActual=planosActual[j]
                planoParaSiguiente=planosSiguiente[j]
                self.SubCubos[valorActual].orientacionColoresActual[planoParaActual]=self.SubCubos[siguienteValor].orientacionColoresActual[planoParaSiguiente]


        valorActual=valoresRotar[len(valoresRotar)-1]
        siguienteValor=valoresRotar[0]
        self.SubCubos[valorActual].copiarSubCubo(subCuboAuxiliar)
        self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
        planosSiguiente = self.convertirPosicionLinealEnCoordenadasPlanosFrontal(siguienteValor)
        planosActual = self.convertirPosicionLinealEnCoordenadasPlanosFrontal(valorActual)
        self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
        for j in range(len(planosSiguiente)):
                planoParaActual=planosActual[j]
                planoParaSiguiente=planosSiguiente[j]
                self.SubCubos[valorActual].orientacionColoresActual[planoParaActual]=subCuboAuxiliar.orientacionColoresActual[planoParaSiguiente]


    def rotarValoresIzquierdaReloj(self,valoresRotar):
        cantidadValores=len(valoresRotar)
        subCuboAuxiliar=SubCubo(0,0,0,0,0)
        subCuboAuxiliar.copiarSubCubo(self.SubCubos[valoresRotar[0]])
        for i in range(0,cantidadValores-1,1):
            valorActual=valoresRotar[i]
            siguienteValor=valoresRotar[i+1]

            self.SubCubos[valorActual].copiarSubCubo(self.SubCubos[siguienteValor])
            posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
            self.SubCubos[valorActual].posicionActual=posicionActual

            planosSiguiente= self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(siguienteValor)
            planosActual= self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(valorActual)
            self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
            for j in range(len(planosSiguiente)):
                planoParaActual=planosActual[j]
                planoParaSiguiente=planosSiguiente[j]

                orientacionActual=self.SubCubos[valorActual].orientacionColoresActual
                orientacionSiguiente=self.SubCubos[siguienteValor].orientacionColoresActual
                self.SubCubos[valorActual].orientacionColoresActual[planoParaActual]=self.SubCubos[siguienteValor].orientacionColoresActual[planoParaSiguiente]
            subcubo=self.SubCubos[valorActual]
            a=1

        valorActual=valoresRotar[len(valoresRotar)-1]
        siguienteValor=valoresRotar[0]
        self.SubCubos[valorActual].copiarSubCubo(subCuboAuxiliar)
        self.SubCubos[valorActual].posicionActual=self.convertirPosicionLinealEnCoordenadas(valorActual)
        planosSiguiente = self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(siguienteValor)
        planosActual = self.convertirPosicionLinealEnCoordenadasPlanosIzquierda(valorActual)
        self.SubCubos[valorActual].orientacionColoresActual=[0,0,0,0,0,0]
        for j in range(len(planosSiguiente)):
                planoParaActual=planosActual[j]
                planoParaSiguiente=planosSiguiente[j]
                self.SubCubos[valorActual].orientacionColoresActual[planoParaActual]=subCuboAuxiliar.orientacionColoresActual[planoParaSiguiente]






