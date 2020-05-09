from modelo.CuboRubik import CuboRubik
from modelo.Nodo import Nodo
from modelo.AEstrella import AEstrella
import copy



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

    # PENDIENTE: algo esta haciendo mal el buscador de soluciones
    # solucionarlo
    solucion=AEstrella.buscarSolucion(nodoInicio,cola,nodosMuertos)

    # PENDIENTE: probar el metodo de medicion de distancia en cubos
    # para dos movimientos al azar la distancia entre el inicio y el final debe ser entre
    # 16 y 32 medido en manhatam
    dibujarSolucion(nodoInicio,solucion)
