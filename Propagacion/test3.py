import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz

# Cargar el archivo JSON
with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/espacios.json', 'r', encoding="utf-8") as f:
    espacios_data = json.load(f)

# Crear instancias de Espacios y Habitabilidad
espacios = []
for key, espacio_data in espacios_data.items():
    habitabilidad_data = espacio_data.pop('habitabilidad')
    habitabilidad = Habitabilidad(**habitabilidad_data)
    fuentes_luz_data = espacio_data.pop('fuentes_luz')
    fuentes_luz = {k: FuenteLuz(**v) for k, v in fuentes_luz_data.items()}
    espacio = Espacios(habitabilidad=habitabilidad, fuentes_luz=fuentes_luz, **espacio_data)
    espacios.append(espacio)

# Modificar las instancias de Espacios y Habitabilidad
for espacio in espacios:
    espacio.habitabilidad.calcular_flujo_luminoso(espacio.get_fuentes_luz())
    espacio.habitabilidad.calcular_iluminancia_prom(factor_mantenimiento=0.8, area=espacio.get_area())
    print(f"Espacio: {espacio.nombre}, Habitabilidad: {espacio.habitabilidad.nivel_habitabilidad}")

# Guardar las instancias modificadas en el archivo JSON
espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in espacios}
with open('c:/Users/jhoja/Documents/GitHub/Proyecto-Habitabilidad/Propagacion/objetos/espacios.json', 'w', encoding="utf-8") as f:
    json.dump(espacios_dict, f, indent=4, ensure_ascii=False)