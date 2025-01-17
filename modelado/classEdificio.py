from modelado.classPared import Pared
from modelado.classEspacios import Espacios

class Edificio:
    def __init__(self, habitaciones: list, paredes: list, matrizConexiones: list, matrizVecindad: list, informacionNodos: str):
        self.habitaciones = habitaciones
        self.paredes = paredes
        self.matrizConexiones = matrizConexiones
        self.matrizVecindad = matrizVecindad
        self.informacionNodos = informacionNodos
    
    def __repr__(self):
        return f"Edificio(habitaciones={self.habitaciones}, paredes={self.paredes}, matrizConexiones={self.matrizConexiones}, matrizVecindad={self.matrizVecindad}, informacionNodos={self.informacionNodos})"
    
    def iniciar_simulacion(self):
        # metodo para iniciar la matriz 
        return False
    
    # Getters y Setters
    def get_habitaciones(self) -> list:
        return self.habitaciones

    def set_habitaciones(self, habitaciones: list):
        self.habitaciones = habitaciones

    def get_paredes(self) -> list:
        return self.paredes

    def set_paredes(self, paredes: list):
        self.paredes = paredes

    def get_matrizConexiones(self) -> list:
        return self.matrizConexiones

    def set_matrizConexiones(self, matrizConexiones: list):
        self.matrizConexiones = matrizConexiones

    def get_matrizVecindad(self) -> list:
        return self.matrizVecindad

    def set_matrizVecindad(self, matrizVecindad: list):
        self.matrizVecindad = matrizVecindad

    def get_informacionNodos(self) -> str:
        return self.informacionNodos

    def set_informacionNodos(self, informacionNodos: str):
        self.informacionNodos = informacionNodos