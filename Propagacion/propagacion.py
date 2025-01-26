from modelado.classEspacios import Espacios
from modelado.classPared import Pared
from typing import List

class PropagacionLuz:
    def __init__(self, espacios: List[Espacios], paredes: List[Pared], matriz_adyacencia):
        self.espacios = {e.id_espacio: e for e in espacios}
        self.paredes = paredes
        self.matriz = matriz_adyacencia  # Matriz cargada desde CSV

    def calcular_propagacion(self):
        for origen_id, espacio_origen in self.espacios.items():
            # Iluminancia interna del espacio (fuentes propias)
            E_interna = espacio_origen.obtener_luz_total()
            
            # Propagación a espacios adyacentes
            for destino_id in self._get_vecinos(origen_id):
                pared = self._buscar_pared(origen_id, destino_id)
                if pared and pared.material.transmision > 0:
                    distancia = self._calcular_distancia(origen_id, destino_id)
                    atenuacion = pared.material.transmision / (distancia ** 2)
                    E_transmitida = E_interna * atenuacion
                    self.espacios[destino_id].habitabilidad.iluminancia_prom += E_transmitida

    def _get_vecinos(self, espacio_id):
        # Obtener IDs de espacios conectados desde la matriz de adyacencia
        return [i for i, val in enumerate(self.matriz[espacio_id-1], 1) if val == 1]

    def _buscar_pared(self, id1, id2):
        for pared in self.paredes:
            if {pared.id_espacio_1, pared.id_espacio_2} == {id1, id2}:
                return pared
        return None

    def _calcular_distancia(self, id1, id2):
        # Ejemplo: distancia = sqrt(área_promedio) como aproximación
        area_prom = (self.espacios[id1].area + self.espacios[id2].area) / 2
        return (area_prom ** 0.5) * 0.5  # Factor de ajuste según disposición