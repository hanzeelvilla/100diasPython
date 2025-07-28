class Quiz:
    def __init__(self, lista):
        self.numero_pregunta = 0
        self.lista_preguntas = lista
    
    def siguiente_pregunta(self):
        pregunta_actual = self.lista_preguntas[self.numero_pregunta]
        self.numero_pregunta += 1
        res = input(f"Q.{self.numero_pregunta}: {pregunta_actual.texto} (true/false)? ")