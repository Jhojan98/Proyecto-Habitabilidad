from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz
from modelado.classActividad import Actividad
from typing import List, Tuple
import json

class Espacios:
    def __init__(self, id_espacio: int, nombre: str, actividad: Actividad, habitabilidad: Habitabilidad, 
                 fuentes_luz: List[Tuple[FuenteLuz, int]], cantidad_personas: int, area: float):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.actividad = actividad
        self.habitabilidad = Habitabilidad(**habitabilidad) if isinstance(habitabilidad, dict) else habitabilidad
        self.fuentes_luz = [(FuenteLuz(**f) if isinstance(f, dict) else f, q) for f, q in fuentes_luz]
        self.cantidad_personas = cantidad_personas
        self.area = area
        self.sugerencias = []
        self.sugerencias_implementadas = []

    def obtener_luz_total(self) -> float:
        """Retorna la iluminancia total del espacio usando los cálculos de habitabilidad."""
        
        return self.habitabilidad.iluminancia_prom
    
    def to_dict(self):
        return {
            "id_espacio": self.id_espacio,
            "nombre": self.nombre,
            "actividad": self.actividad.__dict__,
            "habitabilidad": self.habitabilidad.to_dict(),
            "fuentes_luz": [(fuente.__dict__, cantidad) for fuente, cantidad in self.fuentes_luz],
            "cantidad_personas": self.cantidad_personas,
            "area": self.area,
            "sugerencias": self.sugerencias,
            "sugerencias_implementadas": self.sugerencias_implementadas
        }
    
    # Agregar sugerencias en los nodos necesarios (naranjas y rojos)
    def agregar_sugerencia(self):
        with open("objetos/sugerencias.json", 'r', encoding='utf-8') as f:
            sugerencias = json.load(f)

        iluminancia = self.habitabilidad.iluminancia_prom

        if iluminancia < 0.8*self.actividad.luz_recomendada_min:
            self.sugerencias = sugerencias['implementables']['muy_poca_luz']
        elif iluminancia < self.actividad.luz_recomendada_min:
            self.sugerencias = sugerencias['implementables']['poca_luz']
        elif iluminancia > 1.2*self.actividad.luz_recomendada_max:
            self.sugerencias = sugerencias['implementables']['demasiada_luz']
        elif iluminancia > self.actividad.luz_recomendada_max:
            self.sugerencias = sugerencias['implementables']['mucha_luz']
        else:
            self.sugerencias = []

        # Eliminar las sugerencias que ya han sido implementadas
        for sugerencia in self.sugerencias[:]: # recorrer una copia de la lista ([:])
            if sugerencia in self.sugerencias_implementadas:
                self.sugerencias.remove(sugerencia)

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

    def get_habitabilidad(self) -> Habitabilidad:
        return self.habitabilidad

    def set_habitabilidad(self, habitabilidad: Habitabilidad):
        self.habitabilidad = habitabilidad

    def get_fuentes_luz(self) -> List[Tuple[FuenteLuz, int]]:
        return self.fuentes_luz

    def set_fuentes_luz(self, fuentes_luz: List[Tuple[FuenteLuz, int]]):
        self.fuentes_luz = fuentes_luz

    def get_cantidad_personas(self) -> int:
        return self.cantidad_personas

    def set_cantidad_personas(self, cantidad_personas: int):
        self.cantidad_personas = cantidad_personas

    def get_area(self) -> float:
        return self.area

    def set_area(self, area: float):
        self.area = area