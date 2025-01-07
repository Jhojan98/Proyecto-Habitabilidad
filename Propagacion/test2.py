import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelado.classEdificio import Edificio
from modelado.classEspacios import Espacios
from modelado.classPared import Pared
from modelado.classMaterial import Material

# Helper function to load JSON objects
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# Load Espacios
espacios = []
for i in range(1, 31):
    espacio_dict = load_json(f'objetos/espacios/espacio{i}.json')
    espacios.append(Espacios(**espacio_dict))

# Load Materiales
materiales = []
for i in range(1, 4):
    material_dict = load_json(f'objetos/materiales/material{i}.json')
    materiales.append(Material(**material_dict))

# Load Paredes
paredes = []
for i in range(1, 27):
    pared_dict = load_json(f'objetos/paredes/pared{i}.json')
    paredes.append(Pared(**pared_dict))

# Create an instance of Edificio
edificio = Edificio(
    habitaciones=espacios,
    paredes=paredes,
    matrizConexiones=[[0, 1], [1, 0]],  # Example matrix, should be updated accordingly
    matrizVecindad=[[0, 1], [1, 0]],    # Example matrix, should be updated accordingly
    informacionNodos="Información adicional sobre los nodos"
)



# Save the instance of Edificio to a JSON file
edificio_dict = {
    "habitaciones": [espacio.__dict__ for espacio in edificio.get_habitaciones()],
    "paredes": [pared.to_dict() for pared in edificio.get_paredes()],
    "matrizConexiones": edificio.get_matrizConexiones(),
    "matrizVecindad": edificio.get_matrizVecindad(),
    "informacionNodos": edificio.get_informacionNodos()
}

with open('objetos/edificio.json', 'w', encoding='utf-8') as f:
    json.dump(edificio_dict, f, indent=4, ensure_ascii=False)