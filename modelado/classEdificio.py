import classPared as Pared
import classEspacios as Espacios

class Edificio:
    def __init__(self, habitaciones:Espacios, paredes:Pared, matrizConexiones, matrizVecindad, informacionNodos):
        self.habitaciones = habitaciones
        self.paredes = paredes
        self.matrizConexiones = matrizConexiones
        self.matrizVecindad = matrizVecindad
        self.informacionNodos = informacionNodos
    
    def __repr(self):
        return f"Edificio(habitaciones={self.habitaciones},paredes={self.paredes}, matrizConexiones ={self.matrizConexiones}, matrizVecindad = {self.matrizVecindad}, informacionNodos ={self.informacionNodos} )"
    def iniciar_simulacion():
        #metodo para iniciar la matriz 
        return False