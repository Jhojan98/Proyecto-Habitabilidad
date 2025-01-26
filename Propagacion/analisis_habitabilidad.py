import sys
import os
import json
import pandas as pd
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz
from modelado.classPared import Pared
from modelado.classMaterial import Material
from propagacion import PropagacionLuz

# Cargar el archivo JSON
with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/espacios.json', 'r', encoding="utf-8") as f:
    espacios_data = json.load(f)

# Cargar la matriz de adyacencia desde el archivo CSV
matriz_adyacencia_cargada = pd.read_csv('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/adjacency_matrix.csv', header=None).values

# Cargar las paredes y materiales
with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/paredes.json', 'r', encoding="utf-8") as f:
    paredes_data = json.load(f)

with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/materiales.json', 'r', encoding="utf-8") as f:
    materiales_data = json.load(f)

# Crear instancias de Espacios y Habitabilidad
espacios = []
for key, espacio_data in espacios_data.items():
    habitabilidad_data = espacio_data.pop('habitabilidad')
    habitabilidad = Habitabilidad(**habitabilidad_data)
    fuentes_luz_data = espacio_data.pop('fuentes_luz')
    fuentes_luz = [(FuenteLuz(**fuente_dict), cantidad) for fuente_dict, cantidad in fuentes_luz_data]
    espacio = Espacios(habitabilidad=habitabilidad, fuentes_luz=fuentes_luz, **espacio_data)
    espacios.append(espacio)

# Crear instancias de Paredes
paredes = []
for key, pared_data in paredes_data.items():
    material_data = materiales_data[str(pared_data['material']['id_material'])]
    material = Material(**material_data)
    pared = Pared(material, pared_data['id_espacio_1'], pared_data['id_espacio_2'])
    paredes.append(pared)

propagador = PropagacionLuz(espacios, paredes, matriz_adyacencia_cargada)

# Modificar las instancias de Espacios y Habitabilidad
print("\n============================================= Estado Inicial de los Espacios ==========================================")
for espacio in espacios:
    espacio.habitabilidad.calcular_flujo_luminoso(espacio.get_fuentes_luz())
    espacio.habitabilidad.calcular_iluminancia_prom(factor_mantenimiento=0.8, area=espacio.get_area())
    espacio.habitabilidad.calcular_nivel_habitabilidad(espacio.get_area())
    print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
    print(f"  Iluminancia inicial: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
    print(f"  Nivel habitabilidad inicial: {espacio.habitabilidad.nivel_habitabilidad}")

# Realizar la propagación
print("\n============================================= Realizando propagación de luz ==========================================")

propagador.calcular_propagacion()

print("\n============================================= Estado Final de los Espacios ==========================================")
for espacio in espacios:
    print(f"Espacio {espacio.id_espacio} - {espacio.nombre}:")
    print(f"  Iluminancia final: {espacio.habitabilidad.iluminancia_prom:.2f} lux")
    espacio.habitabilidad.calcular_nivel_habitabilidad(espacio.get_area())
    print(f"  Nivel habitabilidad final: {espacio.habitabilidad.nivel_habitabilidad}")
    #print(f"  Diferencia de iluminancia: {espacio.habitabilidad.iluminancia_prom - espacio.habitabilidad.get_flujo_luminoso():.2f} lux")

# Guardar las instancias modificadas en el archivo JSON
espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in espacios}
with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/espacios.json', 'w', encoding="utf-8") as f:
    json.dump(espacios_dict, f, indent=4, ensure_ascii=False)