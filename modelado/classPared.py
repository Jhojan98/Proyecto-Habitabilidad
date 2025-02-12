from modelado.classMaterial import Material
from modelado.classEspacios import Espacios

class Pared:
    def __init__(self, material: Material, id_espacio_1: int, id_espacio_2: int):
        self.material = Material(**material) if isinstance(material, dict) else material
        self.id_espacio_1 = id_espacio_1
        self.id_espacio_2 = id_espacio_2
    
    def to_dict(self):
        return {
            "material": self.material.to_dict() if self.material else None,
            "id_espacio_1": self.id_espacio_1,
            "id_espacio_2": self.id_espacio_2
        }
    
    # Getters y Setters
    
    def get_material(self) -> Material:
        return self.material

    def set_material(self, material: Material):
        self.material = material

    def get_id_espacio_1(self) -> int:
        return self.id_espacio_1

    def set_id_espacio_1(self, id_espacio_1: int):
        self.id_espacio_1 = id_espacio_1

    def get_id_espacio_2(self) -> int:
        return self.id_espacio_2

    def set_id_espacio_2(self, id_espacio_2: int):
        self.id_espacio_2 = id_espacio_2