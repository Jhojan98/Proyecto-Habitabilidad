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
os.makedirs('objetos', exist_ok=True)

# Crear instancias de la clase Habitabilidad
habitabilidad1 = Habitabilidad(
    id_habitabilidad=1,
    luz_recomendada="500 lux",
    nivel_habitabilidad=85,
    flujo_luminoso=5000.0,
    coeficiente_utilizacion_luz=0.75,
    reduccion_luminosidad=0.1,
    iluminancia_prom=0.0,
    uniformidad_iluminancia=0.0
)

habitabilidad2 = Habitabilidad(
    id_habitabilidad=2,
    luz_recomendada="300 lux",
    nivel_habitabilidad=70,
    flujo_luminoso=3000.0,
    coeficiente_utilizacion_luz=0.8,
    reduccion_luminosidad=0.05,
    iluminancia_prom=0.0,
    uniformidad_iluminancia=0.0
)

habitabilidad3 = Habitabilidad(
    id_habitabilidad=3,
    luz_recomendada="700 lux",
    nivel_habitabilidad=90,
    flujo_luminoso=7000.0,
    coeficiente_utilizacion_luz=0.9,
    reduccion_luminosidad=0.02,
    iluminancia_prom=0.0,
    uniformidad_iluminancia=0.0
)

# Crear instancias de la clase FuenteLuz
fuente_luz1 = FuenteLuz(
    id_fuente_luz=1,
    tipo_fuente="LED",
    interna=True,
    iluminacion_promedio=300.0,
    temperatura_emitida=3500.0,
    intensidad=0.8,
    lumens=3000
)

fuente_luz2 = FuenteLuz(
    id_fuente_luz=2,
    tipo_fuente="Halógena",
    interna=False,
    iluminacion_promedio=500.0,
    temperatura_emitida=2700.0,
    intensidad=1.2,
    lumens=1200
)

fuente_luz3 = FuenteLuz(
    id_fuente_luz=3,
    tipo_fuente="Fluorescente",
    interna=True,
    iluminacion_promedio=400.0,
    temperatura_emitida=3000.0,
    intensidad=1.0,
    lumens=1000
)

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

# Crear instancias de la clase Espacios para el Piso 1
espacios_piso1 = [
    Espacios(1, "Laboratorio de Redes y Telemática", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(2, "Laboratorio de Redes Inalámbricas", "Laboratorio", habitabilidad1, {6: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(3, "Sala de Informática 1", "Laboratorio", habitabilidad1, {6: fuente_luz1, 2: fuente_luz2}, 30, 75.0),
    Espacios(4, "Sala de Informática 2", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(5, "Sala de Informática 3", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(6, "Sala de Informática 4", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(7, "Sala de Informática 5", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(8, "Sala de Informática 6", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(9, "Sala de Informática 7", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(10, "Oficina de Sistemas", "Oficina", habitabilidad2, {1: fuente_luz1}, 10, 50.0),
    Espacios(11, "Área de Soporte Técnico y Almacén", "Área de Soporte", habitabilidad2, {1: fuente_luz1}, 10, 50.0),
    Espacios(12, "Cuarto de Monitoreo", "Monitoreo", habitabilidad3, {1: fuente_luz1}, 5, 25.0)
]

# Crear instancias de la clase Espacios para el Piso 2
espacios_piso2 = [
    Espacios(13, "Laboratorio de Electromagnetismo", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(14, "Laboratorio de Circuitos Eléctricos", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(15, "Laboratorio de Electrónica 1", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(16, "Laboratorio de Electrónica 2", "Laboratorio", habitabilidad1, {7: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(17, "Laboratorio de Electrónica 3", "Laboratorio", habitabilidad1, {6: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(18, "Área de Almacenamiento y Taller de Mantenimiento Electrónico", "Área de Almacenamiento", habitabilidad2, {9: fuente_luz1}, 10, 50.0),
    Espacios(19, "Cuarto de Atención a Estudiantes", "Atención a Estudiantes", habitabilidad2, {5: fuente_luz1}, 10, 50.0),
    Espacios(20, "Laboratorio de Circuitos Impresos", "Laboratorio", habitabilidad1, {6: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(21, "Laboratorio de Telecomunicaciones", "Laboratorio", habitabilidad1, {8: fuente_luz1, 2: fuente_luz2}, 30, 100.0),
    Espacios(22, "Laboratorio Especializado de Control", "Laboratorio", habitabilidad1, {9: fuente_luz1, 2: fuente_luz2}, 30, 100.0)
]

# Crear instancias de la clase Espacios para el Piso 3
espacios_piso3 = [
    Espacios(23, "Salón de Clase 1", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(24, "Salón de Clase 2", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(25, "Salón de Clase 3", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(26, "Salón de Clase 4", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(27, "Salón de Clase 5", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(28, "Salón de Clase 6", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(29, "Salón de Clase 7", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0),
    Espacios(30, "Salón de Clase 8", "Salón de Clase", habitabilidad2, {7: fuente_luz1}, 40, 80.0)
]

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

# Guardar las instancias en diccionarios
fuentes_luz_dict = {fuente_luz.id_fuente_luz: fuente_luz.__dict__ for fuente_luz in [fuente_luz1, fuente_luz2, fuente_luz3]}
materiales_dict = {material.id_material: material.__dict__ for material in [material1, material2, material3]}
espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in espacios_piso1 + espacios_piso2 + espacios_piso3}
paredes_dict = {i+1: pared.to_dict() for i, pared in enumerate(paredes)}

# Guardar los diccionarios en archivos JSON
with open('objetos/fuentes_luz.json', 'w', encoding="utf-8") as f:
    json.dump(fuentes_luz_dict, f, indent=4, ensure_ascii=False)

with open('objetos/materiales.json', 'w', encoding="utf-8") as f:
    json.dump(materiales_dict, f, indent=4, ensure_ascii=False)

with open('objetos/espacios.json', 'w', encoding="utf-8") as f:
    json.dump(espacios_dict, f, indent=4, ensure_ascii=False)

with open('objetos/paredes.json', 'w', encoding="utf-8") as f:
    json.dump(paredes_dict, f, indent=4, ensure_ascii=False)