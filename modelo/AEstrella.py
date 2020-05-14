# libreria local para realizar busquedas A*
# esta funcion diverge para cubos mezclados mas de 5 movimientos
# se debe a que la heuristica de manhattan no es lo suficientemente buena.
from modelo.QuickSort import  QuickSort
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
        QuickSort.quickSortList(cola)
