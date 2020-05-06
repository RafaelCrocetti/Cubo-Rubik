from modelo.CuboRubik import CuboRubik
from modelo.Nodo import Nodo


def buscarSolucion(nodoInicio,cola,nodosMuertos):
    nodoActual = nodoInicio
    while not nodoActual.esSolucion():
        nodoActual = cola.pop(0)
        nodosMuertos.append(nodoActual)
        if nodoActual.esSolucion():
            return nodoActual
        nodosHijos = nodoActual.obtenerHijos()
        for nodo in nodosHijos:
            if nodoVivo(nodosMuertos,nodo):
                insertarNodo(cola,nodo)
        ordenarLista(cola)
    return nodoActual

# inserta un nuevo nodo a la cola si es posible
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
def nodoVivo(nodosMuertos, nodo):
    for muerto in nodosMuertos:
        if nodo.esIgual(muerto):
            return False
    return True


# ordena la cola segun un costo basado en la heuristica de distancia al objetivo
# mas la distancia al origen
# PENDIENTE reemplazar por quick sort
def ordenarLista(cola):
    for passnum in range(len(cola) - 1, 0, -1):
        for i in range(passnum):
            costoNodoActual = cola[i].distanciaOrigen   + cola[i].distanciaObjetivo
            costoNodoSiguiente = cola[i + 1].distanciaOrigen   + cola[i+1].distanciaObjetivo
            if costoNodoActual > costoNodoSiguiente:
                temp = cola[i]
                cola[i] = cola[i + 1]
                cola[i + 1] = temp


if __name__ == '__main__':
    cubo=CuboRubik()
    cubo.realizarMovimiento(cubo.generarSecuenciaMezclado(3))

    nodo=Nodo(None,None,cubo)
    nodoInicio = nodo
    cola = []
    nodosMuertos = []
    nodoInicio.distanciaOrigen = 0
    cola.append(nodoInicio)

    solucion=buscarSolucion(nodoInicio,cola,nodosMuertos)
    padre=solucion.nodoPadre
    nodoActual=solucion
    while padre!=None:
        nodoActual.cuboRubik.print()
        print("")
        nodoActual=nodoActual.nodoPadre
        padre=nodoActual.nodoPadre
