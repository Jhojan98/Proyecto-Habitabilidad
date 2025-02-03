from typing import TYPE_CHECKING, List, Tuple
from modelado.classFuenteLuz import FuenteLuz


class Habitabilidad:
    def __init__(self, id_habitabilidad: int, nivel_habitabilidad: int, flujo_luminoso: float,
                 coeficiente_utilizacion_luz: float, reduccion_luminosidad: float, iluminancia_prom: float = 0.0, uniformidad_iluminancia: float = 0.0):
        self.id_habitabilidad = id_habitabilidad
        self.nivel_habitabilidad = nivel_habitabilidad
        self.flujo_luminoso = flujo_luminoso
        self.coeficiente_utilizacion_luz = coeficiente_utilizacion_luz
        self.reduccion_luminosidad = reduccion_luminosidad
        self.iluminancia_prom = iluminancia_prom
        self.uniformidad_iluminancia = uniformidad_iluminancia

    def to_dict(self):
            return {
                "id_habitabilidad": self.id_habitabilidad,
                "nivel_habitabilidad": self.nivel_habitabilidad,
                "flujo_luminoso": self.flujo_luminoso,
                "coeficiente_utilizacion_luz": self.coeficiente_utilizacion_luz,
                "reduccion_luminosidad": self.reduccion_luminosidad,
                "iluminancia_prom": self.iluminancia_prom,
                "uniformidad_iluminancia": self.uniformidad_iluminancia
            }

    def calcular_nivel_habitabilidad(self, area: float, luz_recomendada_min: float, luz_recomendada_max: float) -> float:
        """
        Calcula el nivel de habitabilidad del espacio usando la fórmula:
        E = (Φ * Cu * Fm) / A
        Donde:
        - E: Iluminancia (lux)
        - Φ: Flujo luminoso (lúmenes)
        - Cu: Coeficiente de utilización
        - Fm: Factor de mantenimiento (1 - reducción_luminosidad)
        - A: Área del espacio (m²)
        
        Args:
            area: Área del espacio en m²
            luz_recomendada_min: Valor mínimo de luz recomendada en lux (proporcionado por la clase Actividad)
            luz_recomendada_max: Valor máximo de luz recomendada en lux (proporcionado por la clase Actividad)
        Returns:
            float: Nivel de habitabilidad
        """
        iluminancia = self.iluminancia_prom

        # Determinar nivel de habitabilidad basado en los valores recomendados de la actividad
        if luz_recomendada_min <= iluminancia <= luz_recomendada_max:
            self.nivel_habitabilidad = 100  # Dentro del rango ideal
        elif iluminancia < luz_recomendada_min:
            # Verificar si está en rango aceptable inferior (hasta 40% debajo)
            self.nivel_habitabilidad = 75 if iluminancia >= 0.6 * luz_recomendada_min else 50
        else:  # iluminancia > luz_recomendada_max
            # Verificar si está en rango aceptable
            self.nivel_habitabilidad = 75 if iluminancia <= 1 * luz_recomendada_max else 50
        
        return self.nivel_habitabilidad

    def calcular_flujo_luminoso(self, fuentes_luz: List[Tuple[FuenteLuz, int]], is_night: bool):
        """Calcula el flujo luminoso total de fuentes propias del espacio"""
        self.flujo_luminoso = sum(
            cantidad * fuente.lumens 
            for fuente, cantidad in fuentes_luz 
            if not (fuente.id_fuente_luz == 4 and is_night)  # Excluir luz solar de noche
        )

    def calcular_iluminancia_prom(self, area: float):
        """Calcula iluminancia inicial considerando solo fuentes propias"""
        factor_mantenimiento = 1 - self.reduccion_luminosidad
        self.iluminancia_prom = (
            self.flujo_luminoso * 
            self.coeficiente_utilizacion_luz * 
            factor_mantenimiento
        ) / area
  
    # Getters y Setters
    def get_id_habitabilidad(self) -> int:
        return self.id_habitabilidad

    def set_id_habitabilidad(self, id_habitabilidad: int):
        self.id_habitabilidad = id_habitabilidad

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