class Habitabilidad:
    def __init__(self, id_habitabilidad: int, luz_recomendada: str, nivel_habitabilidad: int, flujo_luminoso: float,
                 coeficiente_utilizacion_luz: float, reduccion_luminosidad: float, iluminancia_prom: float = 0.0, uniformidad_iluminancia: float = 0.0):
        self.id_habitabilidad = id_habitabilidad
        self.luz_recomendada = luz_recomendada
        self.nivel_habitabilidad = nivel_habitabilidad
        self.flujo_luminoso = flujo_luminoso
        self.coeficiente_utilizacion_luz = coeficiente_utilizacion_luz
        self.reduccion_luminosidad = reduccion_luminosidad
        self.iluminancia_prom = iluminancia_prom
        self.uniformidad_iluminancia = uniformidad_iluminancia

    def calcular_habitabilidad():
        """
        Calcula el nivel de habitabilidad del espacio
        """
        pass

    def calcular_flujo_luminoso(self, fuentes_luz: dict):
        """
        Calcula el flujo luminoso total basado en las fuentes de luz proporcionadas.
        """
        self.flujo_luminoso = sum(fuente.lumens * int(cantidad) for cantidad, fuente in fuentes_luz.items())

    def calcular_iluminancia_prom(self, area: float, factor_mantenimiento: float):
        """
        Calcula la iluminancia promedio y la asigna al atributo iluminancia_prom.
        """
        self.iluminancia_prom = (self.flujo_luminoso * self.coeficiente_utilizacion_luz * factor_mantenimiento) / area

    def to_dict(self):
        return {
            "id_habitabilidad": self.id_habitabilidad,
            "luz_recomendada": self.luz_recomendada,
            "nivel_habitabilidad": self.nivel_habitabilidad,
            "flujo_luminoso": self.flujo_luminoso,
            "coeficiente_utilizacion_luz": self.coeficiente_utilizacion_luz,
            "reduccion_luminosidad": self.reduccion_luminosidad,
            "iluminancia_prom": self.iluminancia_prom,
            "uniformidad_iluminancia": self.uniformidad_iluminancia
        }

    # Getters y Setters
    def get_id_habitabilidad(self) -> int:
        return self.id_habitabilidad

    def set_id_habitabilidad(self, id_habitabilidad: int):
        self.id_habitabilidad = id_habitabilidad

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

    def get_coeficiente_utilizacion_luz(self) -> float:
        return self.coeficiente_utilizacion_luz

    def set_coeficiente_utilizacion_luz(self, coeficiente_utilizacion_luz: float):
        self.coeficiente_utilizacion_luz = coeficiente_utilizacion_luz

    def get_reduccion_luminosidad(self) -> float:
        return self.reduccion_luminosidad

    def set_reduccion_luminosidad(self, reduccion_luminosidad: float):
        self.reduccion_luminosidad = reduccion_luminosidad