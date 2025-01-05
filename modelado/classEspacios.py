import classHabitabilidad as Habitabilidad

class Espacios:
    def __init__(self, id_espacio, nombre, actividad, habitabilidad:Habitabilidad,
                 cantidad_personas,flujo_luminoso,area, coeficiente_utilizacion_luz,
                 reduccion_luminosidad):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.actividad = actividad
        self.habitabilidad = habitabilidad
        self.cantidad_personas = cantidad_personas
        self.flujo_luminoso = flujo_luminoso
        self.area = area
        self.coeficiente_utilzacion_luz = coeficiente_utilizacion_luz
        self.reduccion_luminosidad = reduccion_luminosidad
    def obtener_luz_total():
        return False
    def movilizar_actividad():
        return False