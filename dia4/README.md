# Día 4

## Modulo Random
- Un módulo es un código/script aislado con una funcionalidad en específico
- Python usa Mersenne Twister para generar números aleatorios

### Ejemplo básico
```python
import random

inicio = 1
fin = 10

# Generar números aleatorios enteros 1 - 10
print(random.randint(inicio, fin))

# Generar números aleatorios float 0 - 1
print(random.random())

# Generar números aleatorios float 1 - 9
print(random.random() * 10)

# Generar números aleatorios float 1.00 - 9.00
print(round(random.random() * 10, 2))
```

### Documentacion
- [Oficial](https://docs.python.org/3/library/random.html)
- [W3schools](https://www.w3schools.com/python/module_random.asp)

## Crear módulos propios

`my_module.py`
```python
num_favorito = 24
```

`main.py`
```python
import my_module
print(my_module.num_favorito)
```

## Lists
[Documentacion](https://docs.python.org/3/tutorial/datastructures.html)

- Es una **estructura de datos**
- Guardar elementos en común
- Tiene orden

```python
frutas = ["manzana", "limón", "sandía"]
print(frutas[0]) # manzana
print(frutas[-1]) # sandía
```