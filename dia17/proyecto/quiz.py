class Quiz:
    def __init__(self, lista):
        self.numero_pregunta = 0
        self.lista_preguntas = lista
        self.score = 0
    
    def hay_preguntas(self):
        return self.numero_pregunta < len(self.lista_preguntas)

    def siguiente_pregunta(self):
        pregunta_actual = self.lista_preguntas[self.numero_pregunta]
        self.numero_pregunta += 1
        res = input(f"Q.{self.numero_pregunta}: {pregunta_actual.texto} (true/false)? ")
        self.comprobar_respuesta(res, pregunta_actual.respuesta)

    def comprobar_respuesta(self, res_usuario, res_correcta):
        if res_usuario.lower() == res_correcta.lower():
            print("Correcto")
            self.score += 1
        else:
            print("Incorrecto")
        
        print(f"La respuesta correcta es {res_correcta}")