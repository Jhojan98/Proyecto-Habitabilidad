from .classPared import Pared
from .classEspacios import Espacios
from .classHabitabilidad import Habitabilidad
from .classFuenteLuz import FuenteLuz
from .classMaterial import Material
from .classActividad import Actividad
from typing import List
import json
import pandas as pd
import numpy as np

class Edificio:
    def __init__(self, habitaciones: list, paredes: list, matrizConexiones: list = None, informacionNodos: str = None):
        self.habitaciones = {h.id_espacio: h for h in habitaciones}  # Convert to dictionary for easier access
        self.paredes = paredes
        self.matrizConexiones = pd.read_csv('objetos/adjacency_matrix.csv', header=None).values if matrizConexiones is None else matrizConexiones
        self.informacionNodos = informacionNodos if informacionNodos is not None else ""
        
    @classmethod
    def cargar_desde_json(cls, ruta_archivo: str = 'objetos/edificio.json'):
        """Carga un edificio desde un archivo JSON"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Crear instancias de espacios
        espacios = []
        for espacio_data in data['habitaciones']:
            # Crear instancia de Habitabilidad
            habitabilidad = Habitabilidad(**espacio_data['habitabilidad'])
            
            # Crear instancias de FuenteLuz
            fuentes_luz = [(FuenteLuz(**fuente_dict), cantidad) 
                          for fuente_dict, cantidad in espacio_data['fuentes_luz']]
            
            # Crear instancia de Actividad
            actividad = Actividad(**espacio_data['actividad'])
            
            # Crear una copia del diccionario y eliminar los campos que se manejan por separado
            espacio_dict = espacio_data.copy()
            del espacio_dict['habitabilidad']
            del espacio_dict['fuentes_luz']
            del espacio_dict['actividad']
            
            # Agregar la instancia de actividad al diccionario
            espacio_dict['actividad'] = actividad
            
            espacio = Espacios(habitabilidad=habitabilidad, fuentes_luz=fuentes_luz, **espacio_dict)
            espacios.append(espacio)
        
        # Crear instancias de paredes
        paredes = []
        for pared_data in data['paredes']:
            material = Material(**pared_data['material'])
            pared = Pared(material, pared_data['id_espacio_1'], pared_data['id_espacio_2'])
            paredes.append(pared)
        
        return cls(
            habitaciones=espacios,
            paredes=paredes,
            informacionNodos=data.get('informacionNodos', '')
        )
    
    def to_dict(self):
        return {
            "habitaciones": [habitacion.to_dict() for habitacion in self.habitaciones.values()],
            "paredes": [pared.to_dict() for pared in self.paredes],
            "informacionNodos": self.informacionNodos
        }
    
    def __repr__(self):
        return f"Edificio(habitaciones={self.habitaciones}, paredes={self.paredes}, matrizConexiones={self.matrizConexiones}, informacionNodos={self.informacionNodos})"
    
    def iniciar_simulacion(self):
        # metodo para iniciar la matriz 
        return False
    
    def calcular_propagacion_luz(self):
        """Calcula la propagación de luz entre espacios del edificio"""
        for origen_id, espacio_origen in self.habitaciones.items():
            # Iluminancia interna del espacio (fuentes propias)
            E_interna = espacio_origen.obtener_luz_total()
            
            # Propagación a espacios adyacentes
            for destino_id in self._get_vecinos(origen_id):
                pared = self._buscar_pared(origen_id, destino_id)
                if pared and pared.material.transmision > 0:
                    distancia = self._calcular_distancia(origen_id, destino_id)
                    atenuacion = pared.material.transmision / (distancia ** 2)
                    E_transmitida = E_interna * atenuacion
                    print(f"Luz transmitida a {self.habitaciones[destino_id].nombre} id: {self.habitaciones[destino_id].id_espacio} "
                          f"de {self.habitaciones[origen_id].nombre} id: {origen_id} es de: {E_transmitida:.2f} lux")
                    self.habitaciones[destino_id].habitabilidad.iluminancia_prom += E_transmitida

    def _get_vecinos(self, espacio_id):
        """Obtiene los IDs de espacios conectados desde la matriz de adyacencia"""
        return [i for i, val in enumerate(self.matrizConexiones[espacio_id-1], 1) if val == 1]

    def _buscar_pared(self, id1, id2):
        """Busca la pared que conecta dos espacios"""
        for pared in self.paredes:
            if {pared.id_espacio_1, pared.id_espacio_2} == {id1, id2}:
                return pared
        return None

    def _calcular_distancia(self, id1, id2):
        """Calcula la distancia aproximada entre dos espacios"""
        area_prom = (self.habitaciones[id1].area + self.habitaciones[id2].area) / 2
        return (area_prom ** 0.5) * 0.5  # Factor de ajuste según disposición

    def calcular_habitabilidad(self, is_night: bool):
        """Calcula la habitabilidad de todos los espacios del edificio"""
        # Estado inicial de los espacios
        print("\n============================================= Estado Inicial de los Espacios ==========================================")
        for espacio in self.habitaciones.values():
            espacio.habitabilidad.calcular_flujo_luminoso(espacio.get_fuentes_luz(), is_night)
            espacio.habitabilidad.calcular_iluminancia_prom(espacio.get_area())
            espacio.habitabilidad.calcular_nivel_habitabilidad(
                espacio.get_area(),
                espacio.actividad.luz_recomendada_min,
                espacio.actividad.luz_recomendada_max
            )
            print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
            print(f"  Iluminancia inicial: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
            print(f"  Nivel habitabilidad inicial: {espacio.habitabilidad.nivel_habitabilidad}")

        # Realizar la propagación
        print("\n============================================= Realizando propagación de luz ==========================================")
        self.calcular_propagacion_luz()

        # Estado final de los espacios
        print("\n============================================= Estado Final de los Espacios ==========================================")
        for espacio in self.habitaciones.values():
            print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
            print(f"  Iluminancia final: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
            espacio.habitabilidad.calcular_nivel_habitabilidad(
                espacio.get_area(),
                espacio.actividad.luz_recomendada_min,
                espacio.actividad.luz_recomendada_max
            )
            print(f"  Nivel habitabilidad final: {espacio.habitabilidad.nivel_habitabilidad}")

        # Guardar las instancias modificadas en el archivo JSON
        espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in self.habitaciones.values()}
        with open('objetos/espacios.json', 'w', encoding="utf-8") as f:
            json.dump(espacios_dict, f, indent=4, ensure_ascii=False)

    # Getters y Setters
    def get_habitaciones(self) -> list:
        return self.habitaciones

    def set_habitaciones(self, habitaciones: list):
        self.habitaciones = habitaciones

    def get_paredes(self) -> list:
        return self.paredes

    def set_paredes(self, paredes: list):
        self.paredes = paredes

    def get_matrizConexiones(self) -> list:
        return self.matrizConexiones

    def set_matrizConexiones(self, matrizConexiones: list):
        self.matrizConexiones = matrizConexiones

    def get_informacionNodos(self) -> str:
        return self.informacionNodos

    def set_informacionNodos(self, informacionNodos: str):
        self.informacionNodos = informacionNodos