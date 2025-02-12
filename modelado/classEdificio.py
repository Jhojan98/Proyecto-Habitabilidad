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
import copy

class Edificio:
    def __init__(self, habitaciones: list, paredes: list, ruta_archivo: str, matrizConexiones: list = None):
        self.habitaciones = {h.id_espacio: h for h in habitaciones}  # Convert to dictionary for easier access
        self.paredes = paredes
        self.ruta_archivo = ruta_archivo
        self.matrizConexiones = pd.read_csv('objetos/adjacency_matrix.csv', header=None).values if matrizConexiones is None else matrizConexiones
        
    @classmethod
    # def cargar_desde_json(cls, ruta_archivo: str = 'objetos/edificio.json'):
    def cargar_desde_json(cls, ruta_archivo: str):
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
            del espacio_dict['sugerencias']
            del espacio_dict['sugerencias_implementadas']
            
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
            ruta_archivo=ruta_archivo
        )
    
    def to_dict(self):
        return {
            "habitaciones": [habitacion.to_dict() for habitacion in self.habitaciones.values()],
            "paredes": [pared.to_dict() for pared in self.paredes]
        }
    
    def __repr__(self):
        return f"Edificio(habitaciones={self.habitaciones}, paredes={self.paredes}, matrizConexiones={self.matrizConexiones}"
    
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

        with open(self.ruta_archivo, 'w', encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

    def implementar_sugerencias(self, edificio_2):
        """Aplica las sugerencias de mejora a los espacios del edificio"""

        print("\n============================================= Sugerencias aplicadas ==========================================")

        still_activities = ['Monitoreo', 'Cuarto Oscuro de Fotografía'] # actividades que no se pueden mover
        espaces_to_move = [] 
        # encontrar espacios que se pueden mover 
        for espacio in self.habitaciones.values():
            if 'Movilizar actividad' in espacio.sugerencias and espacio.actividad.nombre not in still_activities:
                espaces_to_move.append(espacio)

        self.movilizar_actividades(espaces_to_move, edificio_2) if espaces_to_move else None

        # aplicar sugerencias
        for espacio in self.habitaciones.values():  
            if espacio.sugerencias:
                print(f"\nSugerencias para el espacio {espacio.id_espacio} - {espacio.nombre}:")
                print("- " + "\n- ".join(espacio.sugerencias))

                print('Sugerencia aplicada:')
                # si ya se implemento la sugerencia de movilizar actividad, no aplicar las demas sugerencias
                if 'Movilizar actividad' in espacio.sugerencias_implementadas and espacio in espaces_to_move:
                    print(f"Se ha movilizado la actividad a otro espacio")
                    continue

                sugerencia = ''

                if 'Usar lamparas de pie de bajo consumo' in espacio.sugerencias:
                    print(f"Se han usado lamparas de pie de bajo consumo")
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 1.22 #aumentar utilizacion de luz en un 22%
                    sugerencia = 'Usar lamparas de pie de bajo consumo'

                if 'Instalar persianas semitransparentes económicas' in espacio.sugerencias:
                    print(f"Se han instalado persianas semitransparentes económicas")
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 0.82 #disminuir utilizacion de luz en un 18%
                    sugerencia = 'Instalar persianas semitransparentes económicas'

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
                    ), 4)) # agregar 4 luces LED más
                    sugerencia = 'Instalar mas luces LED'

                if 'Instalar cortinas blackout' in espacio.sugerencias:
                    print(f"Se han instalado cortinas blackout") # reducir la luz en un 40%
                    espacio.habitabilidad.reduccion_luminosidad *= 1.4 # aumentar la reducción de luminosidad en un 40%
                    espacio.habitabilidad.coeficiente_utilizacion_luz *= 0.6 # disminuir utilizacion de luz en un 40%
                    sugerencia = 'Instalar cortinas blackout'
                
                if sugerencia != '':
                    espacio.sugerencias_implementadas.append(sugerencia)


    # algoritmo para mover actividades
    def movilizar_actividades(self, espaces_to_move, edificio_2):
        """Mueve la actividad a otro espacio"""
        # encontrar todos las parejas de espacios que pueden intercambiar
        pairs_spaces_can_switch = []
        for espacio in espaces_to_move:
            # print(f"\nEspacio {espacio.id_espacio} - {espacio.actividad.luz_recomendada_min} - {espacio.actividad.luz_recomendada_max}")
            for espacio_destino in espaces_to_move:
                if espacio_destino.id_espacio != espacio.id_espacio:
                    iluminancia = espacio_destino.habitabilidad.iluminancia_prom
                    # print(f"Espacio destino {espacio_destino.id_espacio} - {iluminancia}")
                    if espacio.actividad.luz_recomendada_min <= iluminancia and espacio.actividad.luz_recomendada_max >= iluminancia:
                        # print(f"{espacio_destino.actividad.luz_recomendada_min} - {espacio.habitabilidad.iluminancia_prom} - {espacio_destino.actividad.luz_recomendada_max}")
                        # print(f"El espacio {espacio.id_espacio} se puede mover al espacio {espacio_destino.id_espacio}")
                        
                        pairs_spaces_can_switch.append((espacio, espacio_destino))
        
        # encontrar la mejor pareja para cambiar segun rangos de iluminancia
        best_pairs = []
        best_destination = (None, None, float('inf'))
        for i, pair in enumerate(pairs_spaces_can_switch):
            pairs_list = [pair[0].id_espacio for pair in best_pairs] + [pair[1].id_espacio for pair in best_pairs]

            # si un espacio ya sera movido, no se puede mover de nuevo
            if pair[0].id_espacio in pairs_list:
                continue

            # encontrar la menor diferencia de iluminancia entre la actual y la mejor
            if pair[1].id_espacio not in pairs_list:
                diff = 0
                if pair[0].habitabilidad.iluminancia_prom > pair[1].actividad.luz_recomendada_min and pair[0].habitabilidad.iluminancia_prom < pair[1].actividad.luz_recomendada_max:
                    best_pairs.append(pair)
                    best_destination = (None, None, float('inf'))
                elif pair[0].habitabilidad.iluminancia_prom < pair[1].actividad.luz_recomendada_min:
                    diff = pair[1].actividad.luz_recomendada_min - pair[0].habitabilidad.iluminancia_prom
                else:
                    diff = pair[0].habitabilidad.iluminancia_prom - pair[1].actividad.luz_recomendada_max
                
                best_destination = (pair[0], pair[1], diff) if diff < best_destination[2] else best_destination

            # si el siguiente id de espacio es diferente al actual, agregar la mejor pareja o si es la ultima pareja en la lista
            if (i == len(pairs_spaces_can_switch) - 1) or best_destination[0] is not None and pairs_spaces_can_switch[i+1][0].id_espacio != best_destination[0].id_espacio:
                best_pairs.append((best_destination[0], best_destination[1]))
                best_destination =  (None, None, float('inf'))

        # mover actividades y actualizar json
        for pair in best_pairs:
            safe_espace = copy.deepcopy(pair[0])
            pair[0].nombre = pair[1].nombre
            pair[0].set_actividad(pair[1].actividad)
            pair[1].nombre = safe_espace.nombre
            pair[1].set_actividad(safe_espace.actividad)

            pair[0].sugerencias_implementadas.append('Movilizar actividad')
            pair[1].sugerencias_implementadas.append('Movilizar actividad')
            pair[0].sugerencias_implementadas.append(f'Intercambio con espacio {pair[1].id_espacio}')
            pair[1].sugerencias_implementadas.append(f'Intercambio con espacio {pair[0].id_espacio}')

            # movilizar los mismos espacios para el otro edificio
            safe_espace = None
            for espacio in edificio_2.habitaciones.values():
                if espacio.id_espacio == pair[0].id_espacio:
                    espacio.nombre = pair[0].nombre
                    espacio.set_actividad(pair[0].actividad)
                    espacio.sugerencias_implementadas.append('Movilizar actividad')
                    espacio.sugerencias_implementadas.append(f'Intercambio con espacio {pair[1].id_espacio}')
                if espacio.id_espacio == pair[1].id_espacio:
                    espacio.nombre = pair[1].nombre
                    espacio.set_actividad(pair[1].actividad)
                    espacio.sugerencias_implementadas.append('Movilizar actividad')
                    espacio.sugerencias_implementadas.append(f'Intercambio con espacio {pair[0].id_espacio}')

            print(f"Se ha movido la actividad del espacio {pair[0].id_espacio} al espacio {pair[1].id_espacio}")

            # actualizar json
            with open(self.ruta_archivo, 'w', encoding="utf-8") as f:
                json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)

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

    def set_tiempo(self) -> str:
        return self.set_tiempo

    def set_tiempo(self, set_tiempo: str):
        self.set_tiempo = set_tiempo