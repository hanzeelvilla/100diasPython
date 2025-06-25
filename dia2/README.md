# Día 2

## Tipos de datos
| Tipo de dato     | Ejemplo                 | Descripción                                  |
|------------------|-------------------------|----------------------------------------------|
| `int`            | `42`, `-7`              | Números enteros (positivos o negativos)      |
| `float`          | `3.14`, `-0.001`         | Números decimales (punto flotante)           |
| `str`            | `"hola"`, `'Python'`     | Cadenas de texto                             |
| `bool`           | `True`, `False`          | Booleanos (verdadero o falso)                |
| `list`           | `[1, 2, 3]`, `["a", "b"]`| Lista ordenada y mutable                     |
| `tuple`          | `(1, 2, 3)`              | Tupla ordenada e inmutable                   |
| `dict`           | `{"nombre": "Juan"}`     | Diccionario: pares clave-valor               |
| `set`            | `{1, 2, 3}`              | Conjunto no ordenado de elementos únicos     |
| `NoneType`       | `None`                   | Representa la ausencia de valor              |

> [!NOTE]
> La función `type()` permite saber qel tipo de dato

## Subscripting
Usar corchetes `[]` para acceder a una parte de una colección
```python
print("Hola"[-1])
```

## Type casting
Convertir un tipo de dato a otro
```python
str(123)
int("123")
float(123)
bool(1)
```