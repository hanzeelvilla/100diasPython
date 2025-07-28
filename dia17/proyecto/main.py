from modelo_pregunta import Pregunta
from data import preguntas

banco_preguntas = []

for pregunta in preguntas:
    nueva_pregunta = Pregunta(pregunta["texto"], pregunta["respuesta"])
    banco_preguntas.append(nueva_pregunta)

print(banco_preguntas)