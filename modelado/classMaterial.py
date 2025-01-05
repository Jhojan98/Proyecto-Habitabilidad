class Material:
    def __init__(self,id_material:int,nombre:str,resistencia_luz:int,tipo_material:str):
        self.id_material = id_material
        self.nombre = nombre
        self.resistencia_luz = resistencia_luz
        self.tipo_material = tipo_material

    def evaluar_resistencia():
        """
        Evalua la resistencia que tienen los diferentes materiales
        """

        pass

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