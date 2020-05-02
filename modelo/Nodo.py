from modelo.CuboRubik import CuboRubik
import copy

# modela el comportamiento de un nodo en el grafo de busqueda
class Nodo:
    # todo nodo tiene un nodo padre, un movimiento que lo genero desde su padre
    # y un estado del cubo Rubik asociados
    def __init__(self,padre,movimiento,cubo):
        self.nodoPadre=padre
        self.movimientoGenerador=movimiento
        self.cuboRubik=cubo
        # distancia al nodo objetivo
        self.distanciaObjetivo=self.cuboRubik.hallarDistancaSolucion()
        # comienza como un numero muy grande, deberia ser infinito
        self.distanciaOrigen=10000000

    # verifica si el nodo actual es un nodo solucion
    def esSolucion(self):
        return self.cuboRubik.esSolucion()
    # obtiene los 12 posibles hijos del nodo actual
    def obtenerHijos(self):
        hijos=[]
        for movimiento in self.cuboRubik.movimientosValidos:
            # crea una copia del cubo del nodo actual
            nuevoCubo=copy.deepcopy(self.cuboRubik)
            # realiza un de los 12 movimientos validos
            nuevoCubo.realizarMovimiento(movimiento)
            # crea el nodo hijo a partir del nuevo cubo y su movimiento
            nuevoHijo=Nodo(self,movimiento,nuevoCubo)
            # calcula la distancia al origen del nodo hijo como la distancia actual al origen mas la distancia al hijo
            # desde el nodo actual
            # 16 es la distancia entre un cubo y cualquiera de sus hijos
            nuevoHijo.distanciaOrigen=self.distanciaOrigen+16
            hijos.append(nuevoHijo)
        return hijos

    # halla la distancia Manhattan de un nodo a otro
    def hallarDistanciaNodo(self,nodo):
        return self.cuboRubik.hallarDistanciaACubo(nodo.cuboRubik)

    # verifica si este nodo es igual otro
    def esIgual(self,nodo):
        # lo unico que se verifica es si los cubos son iguales
        return self.cuboRubik.esIgual(nodo.cuboRubik)
