from modelado.classMaterial import Material
from modelado.classEspacios import Espacios

class Pared:
    def __init__(self, material:Material, espacio_1:Espacios ,espacio_2:Espacios):
        self.material= material
        self.espacio_1= espacio_1
        self.espacio_2 = espacio_2
        
    def conectar():
        """
        Conecta dos espacios
        """
        return False
    
    # Getters y Setters
    
    def get_material(self) -> Material:
        return self.material
    def set_material(self, material: Material):
        self.material = material

    def get_espacio_1(self) -> Espacios:
        return self.espacio_1

    def set_espacio_1(self, espacio_1: Espacios):
        self.espacio_1 = espacio_1

    def get_espacio_2(self) -> Espacios:
        return self.espacio_2

    def set_espacio_2(self, espacio_2: Espacios):
        self.espacio_2 = espacio_2