import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz
from modelado.classMaterial import Material
from modelado.classPared import Pared

# Crear carpetas principales para los objetos
os.makedirs('objetos/habitabilidad', exist_ok=True)
os.makedirs('objetos/fuentes_luz', exist_ok=True)
os.makedirs('objetos/espacios', exist_ok=True)
os.makedirs('objetos/materiales', exist_ok=True)
os.makedirs('objetos/paredes', exist_ok=True)

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
    tipo_fuente_luz="Halógena",
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

# Crear instancias de la clase Espacios
espacio1 = Espacios(
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

espacio2 = Espacios(
    id_espacio=2,
    nombre="Oficina",
    actividad="Trabajo",
    id_habitabilidad=1,
    ids_fuentes_luz=[1],
    cantidad_personas=10,
    flujo_luminoso=2000.0,
    area=50.0,
    coeficiente_utilizacion_luz=0.8,
    reduccion_luminosidad=0.05
)

# Guardar las instancias de Espacios en archivos JSON
espacio1_dict = espacio1.__dict__
with open('objetos/espacios/espacio1.json', 'w') as f:
    json.dump(espacio1_dict, f, indent=4)

espacio2_dict = espacio2.__dict__
with open('objetos/espacios/espacio2.json', 'w') as f:
    json.dump(espacio2_dict, f, indent=4)

# Crear objetos de Material y Pared
material = Material(
    id_material=1,
    nombre="Concreto",
    resistencia_luz=5,
    tipo_material="Solido"
)

pared = Pared(
    id_material=1,
    id_espacio_1=1,
    id_espacio_2=2
)

# Guardar los objetos de Material y Pared en archivos JSON
material_dict = material.__dict__
with open('objetos/materiales/material.json', 'w') as f:
    json.dump(material_dict, f, indent=4)

pared_dict = pared.__dict__
with open('objetos/paredes/pared.json', 'w') as f:
    json.dump(pared_dict, f, indent=4)

# Ejemplo de carga y modificación de archivos JSON
# Cargar la instancia desde el archivo JSON y modificarla
with open('objetos/espacios/espacio1.json', 'r') as f:
    espacio_cargado_dict = json.load(f)
    espacio_cargado = Espacios(**espacio_cargado_dict)

espacio_cargado.set_ids_fuentes_luz([1, 2])

espacio_cargado_dict = espacio_cargado.__dict__
with open('objetos/espacios/espacio1.json', 'w') as f:
    json.dump(espacio_cargado_dict, f, indent=4)
