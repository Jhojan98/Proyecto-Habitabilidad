class FuenteLuz:

    def __init__(self, id_fuente_luz: int, tipo_fuente: str,
                 interna: bool, iluminacion_promedio: float, temperatura_emitida: float,
                 intensidad: float, lumens: int):
        self.id_fuente_luz = id_fuente_luz
        self.tipo_fuente = tipo_fuente
        self.interna = interna
        self.iluminacion_promedio = iluminacion_promedio
        self.temperatura_emitida = temperatura_emitida
        self.intensidad = intensidad
        self.lumens = lumens
    
    def calcular_impacto():
        """
        Calcula el impacto de la fuente de luz en el espacio
        """
        pass

    # Getters y Setters
    def get_id_fuente_luz(self) -> int:
        return self.id_fuente_luz

    def set_id_fuente_luz(self, id_fuente_luz: int):
        self.id_fuente_luz = id_fuente_luz

    def get_tipo_fuente(self) -> str:
        return self.tipo_fuente
    
    def set_tipo_fuente(self, tipo_fuente: str):
        self.tipo_fuente = tipo_fuente

    def get_interna(self) -> bool:
        return self.interna

    def set_interna(self, interna: bool):
        self.interna = interna

    def get_iluminacion_promedio(self) -> float:
        return self.iluminacion_promedio

    def set_iluminacion_promedio(self, iluminacion_promedio: float):
        self.iluminacion_promedio = iluminacion_promedio

    def get_temperatura_emitida(self) -> float:
        return self.temperatura_emitida

    def set_temperatura_emitida(self, temperatura_emitida: float):
        self.temperatura_emitida = temperatura_emitida

    def get_intensidad(self) -> float:
        return self.intensidad

    def set_intensidad(self, intensidad: float):
        self.intensidad = intensidad

    def get_lumens(self) -> int:
        return self.lumens

    def set_lumens(self, lumens: int):
        self.lumens = lumens
