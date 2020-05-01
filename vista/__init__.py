from modelo.CuboRubik import CuboRubik
if __name__ == '__main__':
    cubo=CuboRubik()
    cubo.rotarCaraInferiorHorario()
    cubo.rotarCaraInferiorAntiHorario()
    cubo.print()
