class Visitante:
    def __init__(self, nombre, correo, comentario):
        self.nombre = nombre
        self.correo = correo
        self.comentario = comentario
    def format_doc(self): #Definir la estructura del documento
        return{
            'nombre': self.nombre,
            'correo': self.correo,
            'comentario': self.comentario,
        }