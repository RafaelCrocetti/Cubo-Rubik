from modelo.CuboRubik import CuboRubik
from modelo.Nodo import Nodo
import copy

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
        # el oredenador de la lista esta funcionando para 12 elementos
        # PENDIENTE: el error puedede estar en la generacion de la distancia al origen o
        # la distancia al objetivo(estos dos ultimos comprenden implicitamente una revision del metodo de medicion de distancia)
        # o en el reemplazo de variables en el proceso de busqueda
        # de la solucion
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

# obtiene la lista de movimientos desde el nodo inicial hasta la solucion
def obtenerListaSolucion(nodo):
    padre = nodo.nodoPadre
    nodoActual = nodo
    movimientos=[]
    while padre != None:
        movimientos.append(nodoActual.movimientoGenerador)
        nodoActual = nodoActual.nodoPadre
        padre = nodoActual.nodoPadre
    return invertirLista(movimientos)

# toma una lista y la invierte haciendo del primer elemento el ultimo
def invertirLista(lista):
    listaNueva=[]
    for i in range(len(lista)-1,-1,-1):
        listaNueva.append(lista[i])
    return  listaNueva

# dibuja la solucion desde el nodo inicial hasta el final
# indicando el movimiento realizado a cada paso
def dibujarSolucion(nodoInicial,nodoFinal):
    # se hace esta se hace para no modificar al cubo del nodo inicial
    # cada vez que se corra este metodo
    cuboRevuelto=copy.deepcopy(nodoInicial.cuboRubik)
    listaMovimientos=obtenerListaSolucion(nodoFinal)
    cuboRevuelto.print()
    for movimiento in listaMovimientos:
        cuboRevuelto.realizarMovimiento(movimiento)
        print("Movimiento :"+movimiento)
        cuboRevuelto.print()



if __name__ == '__main__':
    cubo=CuboRubik()
    cubo.realizarMovimiento(cubo.generarSecuenciaMezclado(2))
    nodo=Nodo(None,None,cubo)
    nodoInicio = nodo
    cola = []
    nodosMuertos = []
    nodoInicio.distanciaOrigen = 0
    cola.append(nodoInicio)

    # PENDIENTE: algo esta haciendo mal el buscador de soluciones
    # solucionarlo
    solucion=buscarSolucion(nodoInicio,cola,nodosMuertos)

    # PENDIENTE: probar el metodo de medicion de distancia en cubos
    # para dos movimientos al azar la distancia entre el inicio y el final debe ser entre
    # 16 y 32 medido en manhatam
    dibujarSolucion(nodoInicio,solucion)
