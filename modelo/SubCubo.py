import  math
# representa un subcubo, con su posiciones y orientaciones actual y destino
class SubCubo:
    def __init__(self, posicionActual, posicionObjetivo,colores,orientacionActual,orientacionObjetivo):


        # posicion en el espacio 3d con origen 00 en el la esquina Azul amarilla y naranja mirandola de frente
        # a la cara azul
        # El eje x es la intercepcion de los planos Azul y Naranja
        # el eje y es la intercepcion de los planos Amarillo y Naranja
        # el eje z es la intercepcion de los planos Amarillo y Azul
        # la pocision es un vector de tres coordenadas (x,y,z)
        self.posicionActual=posicionActual
        self.posicionObjetivo=posicionObjetivo

        # identificador unico para el subCubo
        self.id = SubCubo.convertirCoordenadasEnId(self.posicionActual)
        # lista de colores del subcubo
        # puede desde estar vacia para el subCubo del centro hasta puede
        # alojar tres valores como el caso de una esquina
        # cada color tiene asociado un numero que es lo que se imprimira en pantalla
        # Sin Color= 0
        # Verde=1
        # Amarillo=2
        # Rojo=3
        # Blanco=4
        # Naranja=5
        # Azol= 6
        self.colores=colores

        # orientacion en el espacio del subCubo, indica sobre que plano se encuentra cada
        # color asociandole a cada color un numero
        # esta lista se encuentra asociada a la lista de colores como en un hash map
        # se opta por  la siguiente codificacion para las caras:
        # 1: posterior
        # 2: izquierda
        # 3: superior
        # 4: derecha
        # 5: inferior
        # 6: frontal
        # 7: ninguna
        self.orientacionActual=orientacionActual
        self.orientacionObjetivo=orientacionObjetivo

    # trabsforma el subcubo en una copia del otro
    def copiarSubCubo(self,subCubo):
        self.id=subCubo.id
        self.colores=subCubo.colores
        self.posicionActual = subCubo.posicionActual
        self.posicionObjetivo = subCubo.posicionObjetivo
        self.orientacionActual = subCubo.orientacionActual
        self.orientacionObjetivo = subCubo.orientacionObjetivo

    # verifica si el subCubo se encuentra en la posicion y orientacion objetivos
    def enEstadoObjetivo(self):
        for i in range(len(self.posicionActual)):
            if self.posicionActual[i]!=self.posicionObjetivo[i]:
                return False
        for i in range(len(self.orientacionActual)):
            if self.orientacionActual[i]!=self.orientacionObjetivo[i]:
                return False
        return  True

    # verifica si un subCubo es igual a otro
    def esIgual(self,subCubo):
        return self.id==subCubo.id

    # obtiene el color del que esta pintado un plano
    def obtenerColorPlano(self,plano):
        for i in range(len(self.orientacionActual)):
            if self.orientacionActual[i]==plano:
                return self.colores[i]
        # caso de fallo
        return 7

    # obtiene el plano que le corresponde al color pasado como parametro
    def obtenerPlanoColor(self,color):
        for i in range(len(self.orientacionActual)):
            if self.colores[i]==color:
                return self.orientacionActual[i]
        # caso de fallo
        return 7
    # convierte las coordenadas de un SubCubo en un id unico para el mismo
    @staticmethod
    def convertirCoordenadasEnId( coordenadas):
        # por la forma que se eligieron las posiciones de los
        # subcubos en la lista de subcubos cada trio de coordenadas
        # en el espacio da como resultado un numero en ternario que
        # representa una posicion en una lista lineal , al pasar ese numero a
        # decimal se tiene la posicion exacta en la lista que le
        # corresponde a ese subcubo dada su posicion actual en el espacio
        return coordenadas[0] + 3 * coordenadas[1] + 9 * coordenadas[2]

    # convierte un numero decimal en un trio de numeros que representan una posicion
    # en el espacio 3d
    @staticmethod
    def convertirIdEnCoordenadas( lineal):
        # descomponiendo en ternario el emtero recibido
        # se pueden calcular un conjunto de tres coordenadas espaciales
        cociente = math.floor((lineal) / 3)
        x = (lineal) % 3
        y = cociente % 3
        z = math.floor(cociente / 3) % 3
        coordenadas = [x, y, z]
        return coordenadas
