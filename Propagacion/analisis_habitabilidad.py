import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelado.classEdificio import Edificio

def iniciar_simulacion(is_night): # is_night = True si es de noche, False si es de día
    # Cargar el edificio desde el archivo JSON
    edificio = Edificio.cargar_desde_json('objetos/edificio.json')
    
    # Calcular la habitabilidad
    edificio.calcular_habitabilidad(is_night)



if __name__ == '__main__':
    iniciar_simulacion(is_night=True) # True si es de noche, False si es de día