import sys
import os
import json
import pandas as pd
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelado.classEspacios import Espacios
from modelado.classHabitabilidad import Habitabilidad
from modelado.classFuenteLuz import FuenteLuz
from modelado.classMaterial import Material
from modelado.classPared import Pared
from modelado.classActividad import Actividad
from modelado.classEdificio import Edificio

# Crear carpetas principales para los objetos
os.makedirs('objetos', exist_ok=True)
# Crear instancia de edificio

# Crear instancias de la clase Habitabilidad
habitabilidad1 = Habitabilidad(
    id_habitabilidad=1,
    nivel_habitabilidad=85,
    flujo_luminoso=5000.0,
    coeficiente_utilizacion_luz=0.75,
    reduccion_luminosidad=0.1,
    iluminancia_prom=0.0,
    uniformidad_iluminancia=0.0
)

habitabilidad2 = Habitabilidad(
    id_habitabilidad=2,
    nivel_habitabilidad=70,
    flujo_luminoso=3000.0,
    coeficiente_utilizacion_luz=0.8,
    reduccion_luminosidad=0.05,
    iluminancia_prom=0.0,
    uniformidad_iluminancia=0.0
)

habitabilidad3 = Habitabilidad(
    id_habitabilidad=3,
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
    lumens=5000
)

fuente_luz2 = FuenteLuz(
    id_fuente_luz=2,
    tipo_fuente="Halógena",
    interna=False,
    iluminacion_promedio=500.0,
    temperatura_emitida=2700.0,
    intensidad=1.2,
    lumens=3000
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

fuente_luz4 = FuenteLuz(
    id_fuente_luz= 4,
    tipo_fuente= "Solar (A través de vidrio)",
    interna= False,
    iluminacion_promedio= 80000.0,
    temperatura_emitida= 5000.0,
    intensidad= 0.8,
    lumens= 120000
)

# Crear instancias de la clase Material
material1 = Material(
    id_material=1,
    nombre="Concreto",
    resistencia_luz=5,
    tipo_material="Sólido",
    opacidad=0.95,    # Alta opacidad para concreto
    reflexion=0.3,    # Reflexión moderada
    transmision=0.0   # No transmite luz
)

material2 = Material(
    id_material=2,
    nombre="Madera",
    resistencia_luz=3,
    tipo_material="Orgánico",
    opacidad=0.8,     # Opacidad moderada-alta
    reflexion=0.2,    # Baja reflexión
    transmision=0.0   # No transmite luz
)

material3 = Material(
    id_material=3,
    nombre="Vidrio",
    resistencia_luz=2,
    tipo_material="Transparente",
    opacidad=0.1,     # Baja opacidad
    reflexion=0.1,    # Baja reflexión
    transmision=0.8   # Alta transmisión de luz
)

# Crear instancias de actividades base (templates)
actividad_laboratorio = Actividad(
    id=1000,
    nombre="Laboratorio",
    descripcion="Actividades de laboratorio y prácticas",
    tipo="Académica",
    duracion="4 horas",
    fecha_inicio="08:00",
    fecha_fin="18:00",
    espacio_id=None,
    luz_recomendada_min=450,
    luz_recomendada_max=550
)

actividad_oficina = Actividad(
    id=2000,
    nombre="Oficina",
    descripcion="Trabajo administrativo y atención",
    tipo="Administrativa",
    duracion="8 horas",
    fecha_inicio="08:00",
    fecha_fin="17:00",
    espacio_id=None,
    luz_recomendada_min=250,
    luz_recomendada_max=350
)

actividad_soporte = Actividad(
    id=3000,
    nombre="Área de Soporte",
    descripcion="Soporte técnico y almacenamiento",
    tipo="Técnica",
    duracion="8 horas",
    fecha_inicio="08:00",
    fecha_fin="17:00",
    espacio_id=None,
    luz_recomendada_min=250,
    luz_recomendada_max=350
)

actividad_monitoreo = Actividad(
    id=4000,
    nombre="Monitoreo",
    descripcion="Monitoreo y control de sistemas",
    tipo="Técnica",
    duracion="24 horas",
    fecha_inicio="00:00",
    fecha_fin="23:59",
    espacio_id=None,
    luz_recomendada_min=600,
    luz_recomendada_max=800
)

actividad_clase = Actividad(
    id=5000,
    nombre="Salón de Clase",
    descripcion="Actividades académicas en aula",
    tipo="Académica",
    duracion="2 horas",
    fecha_inicio="07:00",
    fecha_fin="21:00",
    espacio_id=None,
    luz_recomendada_min=250,
    luz_recomendada_max=350
)

actividad_fotografia = Actividad(
    id=6000,
    nombre="Cuarto Oscuro de Fotografía",
    descripcion="Procesamiento y revelado de fotografías",
    tipo="Técnica",
    duracion="6 horas",
    fecha_inicio="08:00",
    fecha_fin="20:00",
    espacio_id=None,
    luz_recomendada_min=50,
    luz_recomendada_max=100
)

def crear_actividad_unica(actividad_base, espacio_id):
    """Crea una instancia única de actividad para cada espacio."""
    nueva_actividad = Actividad(
        id=actividad_base.id + espacio_id,
        nombre=actividad_base.nombre,
        descripcion=actividad_base.descripcion,
        tipo=actividad_base.tipo,
        duracion=actividad_base.duracion,
        fecha_inicio=actividad_base.fecha_inicio,
        fecha_fin=actividad_base.fecha_fin,
        espacio_id=espacio_id,
        luz_recomendada_min=actividad_base.luz_recomendada_min,
        luz_recomendada_max=actividad_base.luz_recomendada_max
    )
    return nueva_actividad

# Crear instancias de la clase Espacios para el Piso 1
espacios_piso1 = [
    Espacios(1, "Laboratorio de Redes y Telemática", crear_actividad_unica(actividad_laboratorio, 1), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(2, "Laboratorio de Redes Inalámbricas", crear_actividad_unica(actividad_laboratorio, 2), habitabilidad1, [(fuente_luz1, 6), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 90.0),
    Espacios(3, "Sala de Informática 1", crear_actividad_unica(actividad_laboratorio, 3), habitabilidad1, [(fuente_luz1, 6), (fuente_luz2, 3), (fuente_luz4, 1)], 30, 75.0),
    Espacios(4, "Sala de Informática 2", crear_actividad_unica(actividad_laboratorio, 4), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 80.0),
    Espacios(5, "Sala de Informática 3", crear_actividad_unica(actividad_laboratorio, 5), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 4), (fuente_luz4, 1)], 30, 100.0),
    Espacios(6, "Sala de Informática 4", crear_actividad_unica(actividad_laboratorio, 6), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 4), (fuente_luz4, 1)], 30, 80.0),
    Espacios(7, "Sala de Informática 5", crear_actividad_unica(actividad_laboratorio, 7), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 4), (fuente_luz4, 1)], 30, 75.0),
    Espacios(8, "Sala de Informática 6", crear_actividad_unica(actividad_laboratorio, 8), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 4), (fuente_luz4, 1)], 30, 100.0),
    Espacios(9, "Sala de Informática 7", crear_actividad_unica(actividad_laboratorio, 9), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(10, "Oficina de Sistemas", crear_actividad_unica(actividad_oficina, 10), habitabilidad2, [(fuente_luz1, 1), (fuente_luz4, 1)], 10, 50.0),
    Espacios(11, "Área de Soporte Técnico y Almacén", crear_actividad_unica(actividad_soporte, 11), habitabilidad2, [(fuente_luz1, 1)], 10, 50.0),
    Espacios(12, "Cuarto de Monitoreo", crear_actividad_unica(actividad_monitoreo, 12), habitabilidad3, [(fuente_luz1, 1), (fuente_luz4, 1)], 5, 25.0)
]

# Crear instancias de la clase Espacios para el Piso 2 (incluyendo el cuarto de fotografía)
espacios_piso2 = [
    Espacios(13, "Laboratorio de Electromagnetismo", crear_actividad_unica(actividad_laboratorio, 13), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 95.0),
    Espacios(14, "Laboratorio de Circuitos Eléctricos", crear_actividad_unica(actividad_laboratorio, 14), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(15, "Laboratorio de Electrónica 1", crear_actividad_unica(actividad_laboratorio, 15), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(16, "Laboratorio de Electrónica 2", crear_actividad_unica(actividad_laboratorio, 16), habitabilidad1, [(fuente_luz1, 7), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(17, "Laboratorio de Electrónica 3", crear_actividad_unica(actividad_laboratorio, 17), habitabilidad1, [(fuente_luz1, 6), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(18, "Área de Almacenamiento y Taller de Mantenimiento Electrónico", crear_actividad_unica(actividad_soporte, 18), habitabilidad2, [(fuente_luz1, 9), (fuente_luz4, 1)], 10, 50.0),
    Espacios(19, "Cuarto de Atención a Estudiantes", crear_actividad_unica(actividad_oficina, 19), habitabilidad2, [(fuente_luz1, 5), (fuente_luz4, 1)], 10, 50.0),
    Espacios(20, "Laboratorio de Circuitos Impresos", crear_actividad_unica(actividad_laboratorio, 20), habitabilidad1, [(fuente_luz1, 6), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 80.0),
    Espacios(21, "Laboratorio de Telecomunicaciones", crear_actividad_unica(actividad_laboratorio, 21), habitabilidad1, [(fuente_luz1, 8), (fuente_luz2, 2), (fuente_luz4, 1)], 30, 85.0),
    Espacios(22, "Cuarto Oscuro de Fotografía", crear_actividad_unica(actividad_fotografia, 22), habitabilidad1, [(fuente_luz1, 2)], 5, 40.0)
]

# Crear instancias de la clase Espacios para el Piso 3
espacios_piso3 = [
    Espacios(23, "Salón de Clase 1", crear_actividad_unica(actividad_clase, 23), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(24, "Salón de Clase 2", crear_actividad_unica(actividad_clase, 24), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(25, "Salón de Clase 3", crear_actividad_unica(actividad_clase, 25), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(26, "Salón de Clase 4", crear_actividad_unica(actividad_clase, 26), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(27, "Salón de Clase 5", crear_actividad_unica(actividad_clase, 27), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(28, "Salón de Clase 6", crear_actividad_unica(actividad_clase, 28), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(29, "Salón de Clase 7", crear_actividad_unica(actividad_clase, 29), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0),
    Espacios(30, "Salón de Clase 8", crear_actividad_unica(actividad_clase, 30), habitabilidad2, [(fuente_luz1, 7), (fuente_luz4, 1)], 40, 80.0)
]

# Crear instancias de la clase Pared basadas en la matriz de adyacencia
matriz_adyacencia = pd.read_csv('objetos/adjacency_matrix.csv', header=None).values

def obtener_piso(id_espacio):
    if 1 <= id_espacio <= 12:
        return 1
    elif 13 <= id_espacio <= 22:
        return 2
    else:
        return 3

def seleccionar_material(id_espacio1, id_espacio2):
    piso1 = obtener_piso(id_espacio1)
    piso2 = obtener_piso(id_espacio2)
    
    # Si los espacios están en pisos diferentes, no deberían tener pared
    if piso1 != piso2:
        return None
    
    # Para espacios del mismo piso
    if piso1 == piso2:
        # Si alguno de los espacios es un laboratorio, usar vidrio para permitir luz natural
        espacio1 = next((e for e in espacios_piso1 + espacios_piso2 + espacios_piso3 if e.id_espacio == id_espacio1), None)
        espacio2 = next((e for e in espacios_piso1 + espacios_piso2 + espacios_piso3 if e.id_espacio == id_espacio2), None)
        
        if espacio1 and espacio2:
            if "Laboratorio" in espacio1.actividad.nombre or "Laboratorio" in espacio2.actividad.nombre:
                return material3  # Vidrio para laboratorios
        
        return material1  # Concreto por defecto para el mismo piso

# Crear paredes basadas en la matriz de adyacencia
paredes = []
for i in range(len(matriz_adyacencia)):
    for j in range(i + 1, len(matriz_adyacencia)):  # Solo la mitad superior de la matriz
        if matriz_adyacencia[i][j] == 1:
            material = seleccionar_material(i + 1, j + 1)
            if material:  # Solo crear la pared si el material no es None
                paredes.append(Pared(material, i + 1, j + 1))

print(f"\nParedes creadas basadas en la matriz de adyacencia:")
for pared in paredes:
    print(f"Pared entre espacios {pared.id_espacio_1} y {pared.id_espacio_2} - Material: {pared.material.nombre}")

# Guardar las instancias en diccionarios
fuentes_luz_dict = {fuente_luz.id_fuente_luz: fuente_luz.__dict__ for fuente_luz in [fuente_luz1, fuente_luz2, fuente_luz3, fuente_luz4]}
materiales_dict = {material.id_material: material.__dict__ for material in [material1, material2, material3]}
espacios_dict = {espacio.id_espacio: espacio.to_dict() for espacio in espacios_piso1 + espacios_piso2 + espacios_piso3}
paredes_dict = {i+1: pared.to_dict() for i, pared in enumerate(paredes)}

edificio = Edificio(
    habitaciones=espacios_piso1 + espacios_piso2 + espacios_piso3,
    paredes=paredes,
)

# Crear carpeta para habitabilidad si no existe
os.makedirs('objetos/habitabilidad', exist_ok=True)

# Guardar los diccionarios en archivos JSON
with open('objetos/fuentes_luz.json', 'w', encoding="utf-8") as f:
    json.dump(fuentes_luz_dict, f, indent=4, ensure_ascii=False)

with open('objetos/materiales.json', 'w', encoding="utf-8") as f:
    json.dump(materiales_dict, f, indent=4, ensure_ascii=False)

with open('objetos/espacios.json', 'w', encoding="utf-8") as f:
    json.dump(espacios_dict, f, indent=4, ensure_ascii=False)

with open('objetos/paredes.json', 'w', encoding="utf-8") as f:
    json.dump(paredes_dict, f, indent=4, ensure_ascii=False)

# Guardar el edificio completo como JSON
with open('objetos/edificio.json', 'w', encoding="utf-8") as f:
    json.dump(edificio.to_dict(), f, indent=4, ensure_ascii=False)

print("\nTodos los archivos JSON han sido creados exitosamente.")
print("El edificio completo ha sido guardado en 'objetos/edificio.json'")

# Crear diccionario de actividades (ahora incluirá todas las actividades únicas)
actividades_dict = {}

# Agregar todas las actividades de los espacios al diccionario
for espacio in espacios_piso1 + espacios_piso2 + espacios_piso3:
    actividades_dict[espacio.actividad.id] = espacio.actividad.to_dict()

# Guardar actividades en JSON
with open('objetos/actividades.json', 'w', encoding="utf-8") as f:
    json.dump(actividades_dict, f, indent=4, ensure_ascii=False)