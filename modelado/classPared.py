from modelado.classMaterial import Material
from modelado.classEspacios import Espacios

class Pared:
    def __init__(self, id_material: int, id_espacio_1: int, id_espacio_2: int):
        self.id_material = id_material
        self.id_espacio_1 = id_espacio_1
        self.id_espacio_2 = id_espacio_2
        
    def conectar(self):
        """
        Conecta dos espacios
        """
        return False
    
    # Getters y Setters
    
    def get_id_material(self) -> int:
        return self.id_material

    def set_id_material(self, id_material: int):
        self.id_material = id_material

    def get_id_espacio_1(self) -> int:
        return self.id_espacio_1

    def set_id_espacio_1(self, id_espacio_1: int):
        self.id_espacio_1 = id_espacio_1

    def get_id_espacio_2(self) -> int:
        return self.id_espacio_2

    def set_id_espacio_2(self, id_espacio_2: int):
        self.id_espacio_2 = id_espacio_2