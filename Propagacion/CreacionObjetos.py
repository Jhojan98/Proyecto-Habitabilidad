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

# Crear instancias de la clase Habitabilidad
habitabilidad1 = Habitabilidad(
    id_habitabilidad=1,
    luz_recomendada="500 lux",
    nivel_habitabilidad=85,
    flujo_luminoso=5000.0
)

habitabilidad2 = Habitabilidad(
    id_habitabilidad=2,
    luz_recomendada="300 lux",
    nivel_habitabilidad=70,
    flujo_luminoso=3000.0
)

habitabilidad3 = Habitabilidad(
    id_habitabilidad=3,
    luz_recomendada="700 lux",
    nivel_habitabilidad=90,
    flujo_luminoso=7000.0
)

# Guardar las instancias de Habitabilidad en archivos JSON
habitabilidad1_dict = habitabilidad1.__dict__
with open('objetos/habitabilidad/habitabilidad1.json', 'w', encoding="utf-8") as f:
    json.dump(habitabilidad1_dict, f, indent=4, ensure_ascii=False)

habitabilidad2_dict = habitabilidad2.__dict__
with open('objetos/habitabilidad/habitabilidad2.json', 'w', encoding="utf-8") as f:
    json.dump(habitabilidad2_dict, f, indent=4, ensure_ascii=False)

habitabilidad3_dict = habitabilidad3.__dict__
with open('objetos/habitabilidad/habitabilidad3.json', 'w', encoding="utf-8") as f:
    json.dump(habitabilidad3_dict, f, indent=4, ensure_ascii=False)

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

fuente_luz3 = FuenteLuz(
    id_fuente_luz=3,
    tipo_fuente_luz="Fluorescente",
    interna=True,
    iluminacion_promedio=400.0,
    temperatura_emitida=3000.0,
    intensidad=1.0,
    lumens=1000
)

# Guardar las instancias de FuenteLuz en archivos JSON
fuente_luz1_dict = fuente_luz1.__dict__
with open('objetos/fuentes_luz/fuente_luz1.json', 'w', encoding="utf-8") as f:
    json.dump(fuente_luz1_dict, f, indent=4, ensure_ascii=False)

fuente_luz2_dict = fuente_luz2.__dict__
with open('objetos/fuentes_luz/fuente_luz2.json', 'w', encoding="utf-8") as f:
    json.dump(fuente_luz2_dict, f, indent=4, ensure_ascii=False)

fuente_luz3_dict = fuente_luz3.__dict__
with open('objetos/fuentes_luz/fuente_luz3.json', 'w', encoding="utf-8") as f:
    json.dump(fuente_luz3_dict, f, indent=4, ensure_ascii=False)

# Crear instancias de la clase Material
material1 = Material(
    id_material=1,
    nombre="Concreto",
    resistencia_luz=5,
    tipo_material="Sólido"
)

material2 = Material(
    id_material=2,
    nombre="Madera",
    resistencia_luz=3,
    tipo_material="Orgánico"
)

material3 = Material(
    id_material=3,
    nombre="Vidrio",
    resistencia_luz=2,
    tipo_material="Transparente"
)

# Guardar las instancias de Material en archivos JSON
material1_dict = material1.__dict__
with open('objetos/materiales/material1.json', 'w', encoding="utf-8") as f:
    json.dump(material1_dict, f, indent=4, ensure_ascii=False)

material2_dict = material2.__dict__
with open('objetos/materiales/material2.json', 'w', encoding="utf-8") as f:
    json.dump(material2_dict, f, indent=4, ensure_ascii=False)

material3_dict = material3.__dict__
with open('objetos/materiales/material3.json', 'w', encoding="utf-8") as f:
    json.dump(material3_dict, f, indent=4, ensure_ascii=False)

# Crear instancias de la clase Espacios para el Piso 1
espacios_piso1 = [
    Espacios(1, "Laboratorio de Redes y Telemática", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(2, "Laboratorio de Redes Inalámbricas", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(3, "Sala de Informática 1", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(4, "Sala de Informática 2", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(5, "Sala de Informática 3", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(6, "Sala de Informática 4", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(7, "Sala de Informática 5", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(8, "Sala de Informática 6", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(9, "Sala de Informática 7", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(10, "Oficina de Sistemas", "Oficina", 2, [1], 10, 2000.0, 50.0, 0.8, 0.05),
    Espacios(11, "Área de Soporte Técnico y Almacén", "Área de Soporte", 2, [1], 10, 2000.0, 50.0, 0.8, 0.05),
    Espacios(12, "Cuarto de Monitoreo", "Monitoreo", 2, [1], 5, 1000.0, 25.0, 0.9, 0.02)
]

# Guardar las instancias de Espacios del Piso 1 en archivos JSON
for espacio in espacios_piso1:
    espacio_dict = espacio.__dict__
    with open(f'objetos/espacios/espacio{espacio.id_espacio}.json', 'w', encoding="utf-8") as f:
        json.dump(espacio_dict, f, indent=4, ensure_ascii=False)

# Crear instancias de la clase Espacios para el Piso 2
espacios_piso2 = [
    Espacios(13, "Laboratorio de Electromagnetismo", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(14, "Laboratorio de Circuitos Eléctricos", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(15, "Laboratorio de Electrónica 1", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(16, "Laboratorio de Electrónica 2", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(17, "Laboratorio de Electrónica 3", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(18, "Área de Almacenamiento y Taller de Mantenimiento Electrónico", "Área de Almacenamiento", 2, [1], 10, 2000.0, 50.0, 0.8, 0.05),
    Espacios(19, "Cuarto de Atención a Estudiantes", "Atención a Estudiantes", 2, [1], 10, 2000.0, 50.0, 0.8, 0.05),
    Espacios(20, "Laboratorio de Circuitos Impresos", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(21, "Laboratorio de Telecomunicaciones", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1),
    Espacios(22, "Laboratorio Especializado de Control", "Laboratorio", 1, [1, 2], 30, 5000.0, 100.0, 0.75, 0.1)
]

# Guardar las instancias de Espacios del Piso 2 en archivos JSON
for espacio in espacios_piso2:
    espacio_dict = espacio.__dict__
    with open(f'objetos/espacios/espacio{espacio.id_espacio}.json', 'w', encoding="utf-8") as f:
        json.dump(espacio_dict, f, indent=4, ensure_ascii=False)

# Crear instancias de la clase Espacios para el Piso 3
espacios_piso3 = [
    Espacios(23, "Salón de Clase 1", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(24, "Salón de Clase 2", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(25, "Salón de Clase 3", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(26, "Salón de Clase 4", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(27, "Salón de Clase 5", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(28, "Salón de Clase 6", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(29, "Salón de Clase 7", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05),
    Espacios(30, "Salón de Clase 8", "Salón de Clase", 2, [1], 40, 3000.0, 80.0, 0.85, 0.05)
]

# Guardar las instancias de Espacios del Piso 3 en archivos JSON
for espacio in espacios_piso3:
    espacio_dict = espacio.__dict__
    with open(f'objetos/espacios/espacio{espacio.id_espacio}.json', 'w', encoding="utf-8") as f:
        json.dump(espacio_dict, f, indent=4, ensure_ascii=False)

# Crear instancias de la clase Pared
paredes = [
    Pared(material1, 1, 2),
    Pared(material2, 2, 3),
    Pared(material3, 3, 4),
    Pared(material1, 4, 5),
    Pared(material2, 5, 6),
    Pared(material3, 6, 7),
    Pared(material1, 7, 8),
    Pared(material2, 8, 9),
    Pared(material3, 9, 10),
    Pared(material1, 10, 11),
    Pared(material2, 11, 12),
    Pared(material3, 13, 14),
    Pared(material1, 14, 15),
    Pared(material2, 15, 16),
    Pared(material3, 16, 17),
    Pared(material1, 17, 18),
    Pared(material2, 18, 19),
    Pared(material3, 19, 20),
    Pared(material1, 20, 21),
    Pared(material2, 21, 22),
    Pared(material3, 23, 24),
    Pared(material1, 24, 25),
    Pared(material2, 25, 26),
    Pared(material3, 26, 27),
    Pared(material1, 27, 28),
    Pared(material2, 28, 29),
    Pared(material3, 29, 30)
]

# Guardar las instancias de Pared en archivos JSON
for i, pared in enumerate(paredes, start=1):
    pared_dict = pared.to_dict()
    with open(f'objetos/paredes/pared{i}.json', 'w', encoding="utf-8") as f:
        json.dump(pared_dict, f, indent=4, ensure_ascii=False)