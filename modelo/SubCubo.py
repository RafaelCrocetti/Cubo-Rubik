
class SubCubo:
    def __init__(self,id, posicionActual, posicionObjetivo,orientacionColoresActual,orientacionColoresObjetivo):
        self.id=id
        self.posicionActual=posicionActual
        self.posicionObjetivo=posicionObjetivo
        self.orientacionColoresActual=orientacionColoresActual
        self.orientacionColoresObjetivo=orientacionColoresObjetivo
    def copiarSubCubo(self,subCubo):
        self.id = subCubo.id
        self.posicionActual = subCubo.posicionActual
        self.posicionObjetivo = subCubo.posicionObjetivo
        self.orientacionColoresActual = subCubo.orientacionColoresActual
        self.orientacionColoresObjetivo = subCubo.orientacionColoresObjetivo
