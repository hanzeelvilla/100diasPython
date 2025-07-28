from modelo_pregunta import Pregunta
from data import preguntas
from quiz import Quiz

banco_preguntas = []

for pregunta in preguntas:
    nueva_pregunta = Pregunta(pregunta["texto"], pregunta["respuesta"])
    banco_preguntas.append(nueva_pregunta)

quiz = Quiz(banco_preguntas)
quiz.siguiente_pregunta()