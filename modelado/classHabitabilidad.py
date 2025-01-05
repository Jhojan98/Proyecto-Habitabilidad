class Habitabilidad:
    def __init__(self, luz_recomendada:str,nivel_habitabilidad:int,flujo_luminoso:float):
        self.luz_recomendada = luz_recomendada
        self.nivel_habitabilidad = nivel_habitabilidad
        self.flujo_luminoso = flujo_luminoso

    def calcular_habitabilidad():
        """
        Calcula el nivel de habitabilidad del espacio
        """
        pass
    # Getters y Setters
    def get_luz_recomendada(self) -> str:
        return self.luz_recomendada
    
    def set_luz_recomendada(self, luz_recomendada: str):
        self.luz_recomendada = luz_recomendada

    def get_nivel_habitabilidad(self) -> int:
        return self.nivel_habitabilidad

    def set_nivel_habitabilidad(self, nivel_habitabilidad: int):
        self.nivel_habitabilidad = nivel_habitabilidad

    def get_flujo_luminoso(self) -> float:
        return self.flujo_luminoso

    def set_flujo_luminoso(self, flujo_luminoso: float):
        self.flujo_luminoso = flujo_luminoso