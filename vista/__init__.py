from modelo.CuboRubik import CuboRubik
from modelo.Manhattan import Manhattan
if __name__ == '__main__':
    cubo=CuboRubik()
    mezclado=cubo.generarSecuenciaMezclado(1)
    print(mezclado)
    cubo.realizarMovimiento(mezclado)
    cubo.print()
    posicion1=[2,1,2]
    posicion2=[1,0,2]
    print(cubo.hallarDistancaSolucion())
