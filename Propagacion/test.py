import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz

"""
Aqui hay un rpoblema con habitabilidad, ya que es una clase que no se puede serializar, por lo que 
yo creo que se puede referenciar mejor una instancia de habitabilidad en lugar de un objeto habitabilidad
ya que json, no acepta eso, y es mucho mas facil ver un objeto en json que una clase(bkl), osea poner id_habitabilidad y ya fue
creamos todos los objetos en json
"""



# Crear una instancia de la clase Habitabilidad
habitabilidad = Habitabilidad(
    id_habitabilidad=1,
    luz_recomendada="500 lux",
    nivel_habitabilidad=85,
    flujo_luminoso=5000.0
)

# Guardar la instancia de Habitabilidad en un archivo JSON
habitabilidad_dict = habitabilidad.__dict__
with open('objetos/habitabilidad/habitabilidad.json', 'w') as f:
    json.dump(habitabilidad_dict, f, indent=4)

# Crear instancias de la clase FuenteLuz
fuente_luz1 = FuenteLuz(
    id_fuente_luz=1,
    tipo_fuente_luz="LED",
    interna=True,
    iluminacion_promedio=300.0,
    temperatura_emitida=3500.0,
    intensidad=0.8,
    lumens=800
)

fuente_luz2 = FuenteLuz(
    id_fuente_luz=2,
    tipo_fuente_luz="Halogena",
    interna=False,
    iluminacion_promedio=500.0,
    temperatura_emitida=2700.0,
    intensidad=1.2,
    lumens=1200
)

# Guardar las instancias de FuenteLuz en archivos JSON
fuente_luz1_dict = fuente_luz1.__dict__
with open('objetos/fuentes_luz/fuente_luz1.json', 'w') as f:
    json.dump(fuente_luz1_dict, f, indent=4)

fuente_luz2_dict = fuente_luz2.__dict__
with open('objetos/fuentes_luz/fuente_luz2.json', 'w') as f:
    json.dump(fuente_luz2_dict, f, indent=4)

# Crear una instancia de la clase Espacios
espacio = Espacios(
    id_espacio=1,
    nombre="Sala de Conferencias",
    actividad="Reuniones",
    id_habitabilidad=1,
    ids_fuentes_luz=[1, 2],
    cantidad_personas=50,
    flujo_luminoso=5000.0,
    area=100.0,
    coeficiente_utilizacion_luz=0.75,
    reduccion_luminosidad=0.1
)



# Guardar la instancia en un archivo JSON
espacio_dict = espacio.__dict__
with open('objetos/espacios/espacio.json', 'w') as f:
    json.dump(espacio_dict, f, indent=4)
    
# Ejemplo de carga y modificacion de archivos JSON
# Cargar la instancia desde el archivo JSON y imprimirla
with open('objetos/espacios/espacio.json', 'r') as f:
    espacio_cargado_dict = json.load(f)
    espacio_cargado = Espacios(**espacio_cargado_dict)

espacio_cargado.set_ids_fuentes_luz([1, 2])

espacio_cargado_dict = espacio_cargado.__dict__
with open('objetos/espacios/espacio.json', 'w') as f:
    json.dump(espacio_cargado_dict, f, indent=4)
