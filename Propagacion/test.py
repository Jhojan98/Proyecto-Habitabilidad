import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad

# Aqui hay un rpoblema con habitabilidad, ya que es una clase que no se puede serializar, por lo que 
# yo creo que se puede referenciar mejor una instancia de habitabilidad en lugar de un objeto habitabilidad
# ya que json, no acepta eso, y es mucho mas facil ver un objeto en json que una clase(bkl), osea poner id_habitabilidad y ya fue
# creamos todos los objetos en json

# Crear una instancia de la clase Habitabilidad
habitabilidad = Habitabilidad(
    luz_recomendada="500 lux",
    nivel_habitabilidad=85,
    flujo_luminoso=5000.0
)

# Crear una instancia de la clase Espacios
espacio = Espacios(
    id_espacio=1,
    nombre="Sala de Conferencias",
    actividad="Reuniones",
    habitabilidad=habitabilidad,
    cantidad_personas=50,
    flujo_luminoso=5000.0,
    area=100.0,
    coeficiente_utilizacion_luz=0.75,
    reduccion_luminosidad=0.1
)

# Usar los setters para asignar valores
espacio.set_id_espacio(1)
espacio.set_nombre("Sala de Conferencias")
espacio.set_actividad("Reuniones")
espacio.set_habitabilidad(habitabilidad)
espacio.set_cantidad_personas(50)
espacio.set_flujo_luminoso(5000.0)
espacio.set_area(100.0)
espacio.set_coeficiente_utilizacion_luz(0.75)
espacio.set_reduccion_luminosidad(0.1)

# Guardar la instancia en un archivo JSON
espacio_dict = espacio.__dict__
with open('espacio.json', 'w') as f:
    json.dump(espacio_dict, f)

# Cargar la instancia desde el archivo JSON y imprimirla
with open('espacio.json', 'r') as f:
    espacio_cargado_dict = json.load(f)
    espacio_cargado = Espacios(**espacio_cargado_dict)

espacio_cargado.set_habitabilidad(0.35)

espacio_cargado_dict = espacio_cargado.__dict__
with open('espacio.json', 'w') as f:
    json.dump(espacio_cargado_dict, f, indent=4)
