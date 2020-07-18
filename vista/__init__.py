import copy

from modelo.AEstrella import AEstrella
from modelo.CuboRubik import CuboRubik
from modelo.Nodo import Nodo
import sys
from twophase import solve


# obtiene la lista de movimientos desde el nodo inicial hasta la solucion
def obtenerListaSolucion(nodo):
    if nodo is not None:
        padre = nodo.nodoPadre
        nodoActual = nodo
        movimientos = []
        while padre != None:
            movimientos.append(nodoActual.movimientoGenerador)
            nodoActual = nodoActual.nodoPadre
            padre = nodoActual.nodoPadre
        return invertirLista(movimientos)
    else:
        return None


# toma una lista y la invierte haciendo del primer elemento el ultimo
def invertirLista(lista):
    listaNueva = []
    for i in range(len(lista) - 1, -1, -1):
        listaNueva.append(lista[i])
    return listaNueva


# dibuja la solucion desde el nodo inicial hasta el final
# indicando el movimiento realizado a cada paso
def dibujarSolucion(nodoInicial, nodoFinal):
    # se hace esta se hace para no modificar al cubo del nodo inicial
    # cada vez que se corra este metodo
    cuboRevuelto = copy.deepcopy(nodoInicial.cuboRubik)
    listaMovimientos = obtenerListaSolucion(nodoFinal)
    cuboRevuelto.print()
    for movimiento in listaMovimientos:
        cuboRevuelto.realizarMovimiento(movimiento)
        print("Movimiento :" + movimiento)
        cuboRevuelto.print()

def ejecutarAEstrella(cubo):
    cubo.realizarMovimiento(cubo.generarSecuenciaMezclado(6))
    nodo = Nodo(None, None, cubo)
    nodoInicio = nodo
    cola = []
    nodosMuertos = []
    nodoInicio.distanciaOrigen = 0
    try:
        solucion = AEstrella.buscarSolucion(nodoInicio, cola, nodosMuertos,300)
        print(obtenerListaSolucion(solucion))
    except:
        print("tiempo maximo excedido, no se encontro solucion")

if __name__ == '__main__':
    sys.setrecursionlimit(10000000)
    cubo="UUULULFLFDUBDRRDBBUFLFFLBRRLDFFDDBUUFBRRLDRUDLBLFBBRRD"
    solucionCubo=solve(cubo)
    print(solucionCubo)
    listaMovimientos=invertirLista(solucionCubo.split(" "))

    cubo = CuboRubik()
    cubo.realizarMovimientoLista(listaMovimientos)
    ejecutarAEstrella(cubo)

    cubos=CuboRubik.generarCubosMezclados(3,5)
    for i in range(len(cubos)):
        cubos[i].print()
        print("")



