class Pregunta:
    def __init__(self, texto, res):
        self.texto = texto
        self.respuesta = res

pregunta1 = Pregunta("1 + 2 = 3?", True)
print(pregunta1.texto)