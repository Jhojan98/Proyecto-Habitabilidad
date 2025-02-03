class Actividad():
    def __init__(self, id, nombre, descripcion, tipo, duracion, fecha_inicio, fecha_fin, espacio_id, luz_recomendada_min, luz_recomendada_max):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.duracion = duracion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.espacio_id = espacio_id
        self.luz_recomendada_min = luz_recomendada_min
        self.luz_recomendada_max = luz_recomendada_max
    
    def __str__(self):
        return f"Actividad: {self.nombre} ({self.id})"
    
    def __repr__(self):
        return f"Actividad: {self.nombre} ({self.id})"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "tipo": self.tipo,
            "duracion": self.duracion,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "espacio_id": self.espacio_id,
            "luz_recomendada_min": self.luz_recomendada_min,
            "luz_recomendada_max": self.luz_recomendada_max
        }          
