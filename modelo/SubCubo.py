
# representa un subcubo, con su posiciones y orientaciones actual y destino
class SubCubo:
    def __init__(self,id, posicionActual, posicionObjetivo,orientacionColoresActual,orientacionColoresObjetivo):
        self.id=id
        # posicion en el espacio 3d con origen 00 en el la esquina Azul amarilla y naranja mirandola de frente
        # a la cara azul
        # El eje x es la intercepcion de los planos Azul y Naranja
        # el eje y es la intercepcion de los planos Amarillo y Naranja
        # el eje z es la intercepcion de los planos Amarillo y Azul
        # la pocision es un vector de tres coordenadas (x,y,z)
        self.posicionActual=posicionActual
        self.posicionObjetivo=posicionObjetivo
        # orientacion en el espacio del subCubo, indica sobre que plano se encuentra cada
        # color asociandole a cada color un numero
        # se opta por  la siguiente codificacion para las caras:
        # 0: posterior
        # 1: izquierda
        # 2: superior
        # 3: derecha
        # 4: inferior
        # 5: frontal
        # 6: ninguna
        # el numero asociado a la cara es la posicion en un vector de 6 elementos
        # estas posiciones pueden ser habitadas por un color
        # esta es la lista de colores del cubo y su representacion como numero
        # colores=["Sin Color","Verde","Amarillo","Rojo","Blanco","Naranja","Azul"]
        # coloresEnNumeros=[0,1,2,3,4,5,6]
        # Sin Color= 0
        # Verde=1
        # Amarillo=2
        # Rojo=3
        # Blanco=4
        # Naranja=5
        # Azol= 6
        # como un maximo de 3 posiciones pueden ser asignadas con colores y como minimo 0
        # esto es exceptuando el subCubo del centro del cubo
        self.orientacionColoresActual=orientacionColoresActual
        self.orientacionColoresObjetivo=orientacionColoresObjetivo

    # trabsforma el subcubo en una copia del otro
    def copiarSubCubo(self,subCubo):
        self.id = subCubo.id
        self.posicionActual = subCubo.posicionActual
        self.posicionObjetivo = subCubo.posicionObjetivo
        self.orientacionColoresActual = subCubo.orientacionColoresActual
        self.orientacionColoresObjetivo = subCubo.orientacionColoresObjetivo

    # verifica si el subCubo se encuentra en la posicion y orientacion objetivos
    def enEstadoObjetivo(self):
        for i in range(len(self.posicionActual)):
            if self.posicionActual[i]!=self.posicionObjetivo[i]:
                return False
        for i in range(len(self.orientacionColoresActual)):
            if self.orientacionColoresActual[i]!=self.orientacionColoresObjetivo[i]:
                return False
        return  True

    def esIgual(self,subCubo):
        return self.id==subCubo.id
