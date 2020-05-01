# libreria local para hallar distancia Manhattan
class Manhattan:
    # halla la distancia manhatam entre dos posiciones en el espacio X,Y,Z
    @staticmethod
    def hallarDistanciaManhattan( posicion1, posicion2):
        distancia = 0
        for i in range(len(posicion1)):
            diferencia = posicion1[i] - posicion2[i]
            if diferencia < 0:
                diferencia = -diferencia
            distancia = distancia + diferencia

        return distancia
