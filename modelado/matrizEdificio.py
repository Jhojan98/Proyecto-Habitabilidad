#aca deberia ir la matriz

class Espacios:
    def __init__(self, id_espacio: int, nombre: str, actividad: str, habitabilidad: float, cantidad_personas: int, flujo_luminoso: float, area: float, coeficiente_utilizacion_luz: float, reduccion_luminosidad: float):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.actividad = actividad
        self.habitabilidad = habitabilidad
        self.cantidad_personas = cantidad_personas
        self.flujo_luminoso = flujo_luminoso
        self.area = area
        self.coeficiente_utilzacion_luz = coeficiente_utilizacion_luz
        self.reduccion_luminosidad = reduccion_luminosidad

    def obtener_luz_total(self) -> bool:
        return False

    def movilizar_actividad(self) -> bool:
        return False

    # Getters y Setters
    def get_id_espacio(self) -> int:
        return self.id_espacio

    def set_id_espacio(self, id_espacio: int):
        self.id_espacio = id_espacio

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_actividad(self) -> str:
        return self.actividad

    def set_actividad(self, actividad: str):
        self.actividad = actividad

    def get_habitabilidad(self) -> float:
        return self.habitabilidad

    def set_habitabilidad(self, habitabilidad: float):
        self.habitabilidad = habitabilidad

    def get_cantidad_personas(self) -> int:
        return self.cantidad_personas

    def set_cantidad_personas(self, cantidad_personas: int):
        self.cantidad_personas = cantidad_personas

    def get_flujo_luminoso(self) -> float:
        return self.flujo_luminoso

    def set_flujo_luminoso(self, flujo_luminoso: float):
        self.flujo_luminoso = flujo_luminoso

    def get_area(self) -> float:
        return self.area

    def set_area(self, area: float):
        self.area = area

    def get_coeficiente_utilizacion_luz(self) -> float:
        return self.coeficiente_utilzacion_luz

    def set_coeficiente_utilizacion_luz(self, coeficiente_utilizacion_luz: float):
        self.coeficiente_utilzacion_luz = coeficiente_utilizacion_luz

    def get_reduccion_luminosidad(self) -> float:
        return self.reduccion_luminosidad

    def set_reduccion_luminosidad(self, reduccion_luminosidad: float):
        self.reduccion_luminosidad = reduccion_luminosidad