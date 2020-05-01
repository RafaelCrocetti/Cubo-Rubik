from modelo.CuboRubik import CuboRubik
from modelo.Manhattan import Manhattan
from modelo.Nodo import Nodo
if __name__ == '__main__':
        cuboRubik=CuboRubik()
        cuboRubik.realizarMovimiento(cuboRubik.generarSecuenciaMezclado(1))
        nodoInicio = Nodo(None,"",cuboRubik)
        cola = []
        nodosMuertos = []
        nodoInicio.distanciaOrigen = 0
        cola.append(nodoInicio)




def buscarSolucion(nodoInicio,cola,nodosMuertos):
    nodoActual = nodoInicio
    while not nodoActual.esSolucion():
        nodoActual = cola.pop(0)
        nodosMuertos.append(nodoActual)
        if nodoActual.esSolucion():
            return nodoActual
        nodosHijos = nodoActual.obtenerHijos()
        for nodo in nodosHijos:
            if self.nodoVivo(nodo):
                self.insertarNodo(nodo)
        self.ordenarLista()
    return nodoActual


def insertarNodo(self, nodoInsertar):
    nodoEnCola = None
    for nodo in self.cola:
        if nodoInsertar.comparar(nodoInsertar) == 0:
            if nodo.distanciaOrigen > nodoInsertar.distanciaOrigen:
                nodo = nodoInsertar
                nodoEnCola = nodo
            break

    if nodoEnCola == None:
        self.cola.append(nodoInsertar)


def nodoVivo(self, nodo):
    for muerto in self.nodosMuertos:
        if nodo.comparar(muerto) == 0:
            return False
    return True


# reemplazar por quick sort
def ordenarLista(self):
    for passnum in range(len(self.cola) - 1, 0, -1):
        for i in range(passnum):
            costoNodoActual = self.cola[i].distanciaOrigen  # +self.cola[i].distanciaObjetivo
            costoNodoSiguiente = self.cola[i + 1].distanciaOrigen  # +self.cola[i+1].distanciaObjetivo
            if costoNodoActual > costoNodoSiguiente:
                temp = self.cola[i]
                self.cola[i] = self.cola[i + 1]
                self.cola[i + 1] = temp
