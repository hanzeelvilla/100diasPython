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

## Operadores matemáticos
| Operador | Símbolo | Ejemplo         | Resultado | Descripción                     |
|----------|---------|------------------|-----------|---------------------------------|
| Suma     | `+`     | `3 + 2`          | `5`       | Suma dos valores                |
| Resta    | `-`     | `5 - 2`          | `3`       | Resta el segundo del primero    |
| Multiplicación | `*` | `4 * 3`        | `12`      | Multiplica dos valores          |
| División | `/`     | `10 / 2`         | `5.0`     | División con resultado flotante |
| División entera | `//` | `10 // 3`    | `3`       | División sin decimales (entera) |
| Módulo   | `%`     | `10 % 3`         | `1`       | Resto de la división            |
| Potencia | `**`    | `2 ** 3`         | `8`       | Exponenciación (potencia)       |

## Operadores de Asignación
| Operador | Ejemplo     | Equivalente     | Descripción                          |
|----------|-------------|------------------|--------------------------------------|
| `=`      | `x = 5`     | —                | Asigna el valor 5 a `x`              |
| `+=`     | `x += 3`    | `x = x + 3`      | Suma y asigna                        |
| `-=`     | `x -= 2`    | `x = x - 2`      | Resta y asigna                       |
| `*=`     | `x *= 4`    | `x = x * 4`      | Multiplica y asigna                  |
| `/=`     | `x /= 2`    | `x = x / 2`      | Divide y asigna (resultado flotante)|
| `//=`    | `x //= 2`   | `x = x // 2`     | División entera y asigna             |
| `%=`     | `x %= 2`    | `x = x % 2`      | Módulo y asigna                      |
| `**=`    | `x **= 3`   | `x = x ** 3`     | Potencia y asigna                    |

# F Strings
Insertar valores de variables dentro de una cadena de texto. Se escribe con la letra `f` al inicio de la cadena, con variables encerradas entre llaves `{}`.
```python
nombre = "Hanzeel"
edad = 21
altura = 1.75
print(f"Me llamo {nombre} tengo {edad} años mido {altura}")
```