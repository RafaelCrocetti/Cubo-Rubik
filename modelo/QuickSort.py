
# libreria local para realizar  orden de listas
# utilizando el algoritmo quicksort
import range as range


class QuickSort:
    @staticmethod
    def quickSortList(lista):
        QuickSort.quickSort(lista,0,len(lista)-1)

    @staticmethod
    def quickSort(lista,inferior,superior):
        if inferior<superior:
            p=QuickSort.particion(lista,inferior,superior)
            QuickSort.quickSort(lista, inferior, p-1)
            QuickSort.quickSort(lista, p+1, superior)

    @staticmethod
    def obtenerPivot(lista,inferior,superior):
        medio=(inferior+superior)//2
        pivot=superior
        if lista[inferior].heurisitca()<lista[medio].heurisitca():
            if lista[medio].heurisitca()<lista[superior].heurisitca():
                pivot=medio
        elif lista[inferior].heurisitca()<lista[superior].heurisitca():
            pivot=inferior
        return pivot

    @staticmethod
    def particion(lista,inferior,superior):
        indicePivot=QuickSort.obtenerPivot(lista,inferior,superior)
        valorPivot=lista[indicePivot].heurisitca()
        lista[indicePivot],lista[inferior]=lista[inferior], lista[indicePivot]

        borde=inferior

        for i in range(inferior,superior+1):
            if lista[i].heurisitca()<valorPivot:
                borde+=1
                lista[i],lista[borde]= lista[borde], lista[i]
            lista[inferior],lista[borde]=lista[borde], lista[inferior]
        return borde
