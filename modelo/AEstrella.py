from modelo.CuboRubik import CuboRubik
from modelo.Nodo import Nodo
import copy
# libreria local para realizar busquedas A*
class AEstrella:

    #busca el nodo solucion dado el nodo inicial, la direccion de una cola
    # y la direccion de una lista de nodos muertos
    @staticmethod
    def buscarSolucion(nodoInicio, cola, nodosMuertos):
        cola.append(nodoInicio)
        nodoActual = nodoInicio
        while not nodoActual.esSolucion():
            nodoActual = cola.pop(0)
            nodosMuertos.append(nodoActual)
            if nodoActual.esSolucion():
                return nodoActual
            nodosHijos = nodoActual.obtenerHijos()
            for nodo in nodosHijos:
                if AEstrella.nodoVivo(nodosMuertos, nodo):
                    AEstrella.insertarNodo(cola, nodo)
            # el oredenador de la lista esta funcionando para 12 elementos
            # PENDIENTE: el error puedede estar en la generacion de la distancia al origen o
            # la distancia al objetivo(estos dos ultimos comprenden implicitamente una revision del metodo de medicion de distancia)
            # o en el reemplazo de variables en el proceso de busqueda
            # de la solucion
            AEstrella.ordenarLista(cola)
        return nodoActual

    # inserta un nuevo nodo a la cola si es posible
    @staticmethod
    def insertarNodo(cola, nodoInsertar):
        nodoEnCola = None
        for nodo in cola:
            if nodoInsertar.esIgual(nodo):
                if nodo.distanciaOrigen > nodoInsertar.distanciaOrigen:
                    nodo = nodoInsertar
                    nodoEnCola = nodo
                break
        if nodoEnCola == None:
            cola.append(nodoInsertar)

    # virifica si el nodo se encuentra en la lista de nodos muertos
    @staticmethod
    def nodoVivo(nodosMuertos, nodo):
        for muerto in nodosMuertos:
            if nodo.esIgual(muerto):
                return False
        return True

    # ordena la cola segun un costo basado en la heuristica de distancia al objetivo
    # mas la distancia al origen
    # PENDIENTE reemplazar por quick sort
    @staticmethod
    def ordenarLista(cola):
        for passnum in range(len(cola) - 1, 0, -1):
            for i in range(passnum):
                costoNodoActual = cola[i].distanciaOrigen + cola[i].distanciaObjetivo
                costoNodoSiguiente = cola[i + 1].distanciaOrigen + cola[i + 1].distanciaObjetivo
                if costoNodoActual > costoNodoSiguiente:
                    temp = cola[i]
                    cola[i] = cola[i + 1]
                    cola[i + 1] = temp