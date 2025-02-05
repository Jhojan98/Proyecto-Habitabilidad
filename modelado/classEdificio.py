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
        # print("\n============================================= Estado Inicial de los Espacios ==========================================")
        for espacio in self.habitaciones.values():
            espacio.habitabilidad.calcular_flujo_luminoso(espacio.get_fuentes_luz(), is_night)
            espacio.habitabilidad.calcular_iluminancia_prom(espacio.get_area())
            espacio.habitabilidad.calcular_nivel_habitabilidad(
                espacio.get_area(),
                espacio.actividad.luz_recomendada_min,
                espacio.actividad.luz_recomendada_max
            )
            # print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
            # print(f"  Iluminancia inicial: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
            # print(f"  Nivel habitabilidad inicial: {espacio.habitabilidad.nivel_habitabilidad}")

        # Realizar la propagación
        print("\n============================================= Realizando propagación de luz ==========================================")
        self.calcular_propagacion_luz()

        # Estado final de los espacios
        # print("\n============================================= Estado Final de los Espacios ==========================================")
        for espacio in self.habitaciones.values():
            # print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
            # print(f"  Iluminancia final: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
            espacio.habitabilidad.calcular_nivel_habitabilidad(
                espacio.get_area(),
                espacio.actividad.luz_recomendada_min,
                espacio.actividad.luz_recomendada_max
            )
            # print(f"  Nivel habitabilidad final: {espacio.habitabilidad.nivel_habitabilidad}")

            # Agregar sugerencias para cada nodo
            espacio.agregar_sugerencia()

        # Guardar las instancias modificadas en el archivo JSON
        espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in self.habitaciones.values()}
        with open('objetos/espacios.json', 'w', encoding="utf-8") as f:
            json.dump(espacios_dict, f, indent=4, ensure_ascii=False)

        with open('objetos/edificio.json', 'w', encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    def aplicar_sugerencias(self):
        """Aplica las sugerencias de mejora a los espacios del edificio"""
        print("\n============================================= Sugerencias aplicadas ==========================================")

        still_activities = ['Laboratorio', 'Monitoreo', 'Cuarto Oscuro de Fotografía']
        espaces_to_move = []
        for espacio in self.habitaciones.values():
            if 'Movilizar actividad' in espacio.sugerencias and espacio.actividad.nombre not in still_activities:
                espaces_to_move.append(espacio)
                espacio.sugerencias.remove('Movilizar actividad')

        # self.movilizar_actividades(espaces_to_move)

        for espacio in self.habitaciones.values():
            # print(espacio not in espaces_to_move)
            if espacio.sugerencias and espacio not in espaces_to_move:
                print(f"\nSugerencias para el espacio {espacio.id_espacio} - {espacio.nombre}:")
                print("- " + "\n- ".join(espacio.sugerencias))

                print('Sugerencia aplicada:')
                if 'Pintar las paredes con colores claros' in espacio.sugerencias:
                    print(f"Se ha pintado el espacio con colores claros")
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 1.18 #aumentar utilizacion de luz en un 18%
                    espacio.sugerencias.remove('Pintar las paredes con colores claros')

                if 'Pintar las paredes con colores oscuros' in espacio.sugerencias:
                    print(f"Se ha pintado el espacio con colores oscuros")
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 0.82 #disminuir utilizacion de luz en un 18%
                    espacio.sugerencias.remove('Pintar las paredes con colores oscuros')


                if 'Instalar mas luces LED' in espacio.sugerencias:
                    print(f"Se han instalado más luces LED")
                    espacio.fuentes_luz.append((FuenteLuz(
                        id_fuente_luz=1,
                        tipo_fuente="LED",
                        interna=True,
                        iluminacion_promedio=300.0,
                        temperatura_emitida=3500.0,
                        intensidad=0.8,
                        lumens=5000
                    ), 2)) # agregar 2 luces LED más
                    espacio.sugerencias.remove('Instalar mas luces LED')

                if 'Instalar cortinas blackout' in espacio.sugerencias:
                    print(f"Se han instalado cortinas blackout") # reducir la luz en un 80%
                    espacio.habitabilidad.reduccion_luminosidad *= 1.8 # aumentar la reducción de luminosidad en un 80%
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 0.2 # disminuir utilizacion de luz en un 80%
                    espacio.sugerencias.remove('Instalar cortinas blackout')
                
    def movilizar_actividades(self, espaces_to_move):
        """Mueve la actividad a otro espacio"""
        # print('Se ha movilizado la actividad a otro espacio')

        space_to_move = {}
        for espacio in espaces_to_move:
            print(f"\nEspacio {espacio.id_espacio} - {espacio.actividad.luz_recomendada_min} - {espacio.actividad.luz_recomendada_max}")
            # for espacio_destino in espaces_to_move:
            for espacio_destino in self.habitaciones.values():
                if espacio_destino.id_espacio != espacio.id_espacio:
                    iluminancia = espacio_destino.habitabilidad.iluminancia_prom
                    print(f"Espacio destino {espacio_destino.id_espacio} - {iluminancia}")
                    # if espacio.actividad.luz_recomendada_min <= iluminancia and espacio.actividad.luz_recomendada_max >= iluminancia:
                    #     print(f"El espacio {espacio.id_espacio} se puede mover al espacio {espacio_destino.id_espacio}")
                    if espacio.actividad.luz_recomendada_min <= iluminancia and espacio.actividad.luz_recomendada_max >= iluminancia and espacio_destino.actividad.luz_recomendada_min <= espacio.habitabilidad.iluminancia_prom and espacio_destino.actividad.luz_recomendada_max >= espacio.habitabilidad.iluminancia_prom:
                        print(f"{espacio_destino.actividad.luz_recomendada_min} - {espacio.habitabilidad.iluminancia_prom} - {espacio_destino.actividad.luz_recomendada_max}")
                        print(f"El espacio {espacio.id_espacio} se puede mover al espacio {espacio_destino.id_espacio}")
        return False

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