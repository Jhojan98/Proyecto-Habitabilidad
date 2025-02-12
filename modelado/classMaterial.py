class Material:
    def __init__(self,id_material:int,nombre:str,resistencia_luz:int,tipo_material:str,
                 opacidad: float = 0.0, reflexion: float = 0.0, transmision: float = 0.0):
        self.id_material = id_material
        self.nombre = nombre
        self.resistencia_luz = resistencia_luz
        self.tipo_material = tipo_material
        self.opacidad = opacidad
        self.reflexion = reflexion
        self.transmision = transmision

    def to_dict(self):
        return {
            "id_material": self.id_material,
            "nombre": self.nombre,
            "resistencia_luz": self.resistencia_luz,
            "tipo_material": self.tipo_material,
            "opacidad": self.opacidad,
            "reflexion": self.reflexion,
            "transmision": self.transmision
        }
    
    # Getters y Setters
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_id_material(self) -> int:
        return self.id_material

    def set_id_material(self, id_material: int):
        self.id_material = id_material

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_resistencia_luz(self) -> int:
        return self.resistencia_luz

    def set_resistencia_luz(self, resistencia_luz: int):
        self.resistencia_luz = resistencia_luz

    def get_tipo_material(self) -> str:
        return self.tipo_material

    def set_tipo_material(self, tipo_material: str):
        self.tipo_material = tipo_material

    def get_opacidad(self) -> float:
        return self.opacidad

    def set_opacidad(self, opacidad: float):
        self.opacidad = opacidad

    def get_reflexion(self) -> float:
        return self.reflexion

    def set_reflexion(self, reflexion: float):
        self.reflexion = reflexion

    def get_transmision(self) -> float:
        return self.transmision

    def set_transmision(self, transmision: float):
        self.transmision = transmision