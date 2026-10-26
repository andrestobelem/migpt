# 01 — Predecir el siguiente carácter

El objetivo es construir una primera distribución de probabilidad sobre el siguiente carácter. Usaremos conteos antes de introducir parámetros entrenables y gradientes.

## Un texto pequeño

Usá este corpus, donde los espacios también cuentan como caracteres:

```python
texto = "banana bandana"
```

Cada carácter será un token. El vocabulario contiene cinco tokens: espacio, `a`, `b`, `d` y `n`. Un identificador numérico representa un token; su valor no expresa orden ni similitud entre caracteres.

Para formar ejemplos, desplazá el texto una posición:

```text
entrada: banana bandan
objetivo: anana bandana
```

Cada pareja contiene un carácter observado y su sucesor real. Hay 13 parejas en este corpus. El último carácter no tiene un sucesor observado: no agregamos una transición del final al principio.

## El modelo

Un modelo de bigramas aproxima la probabilidad del siguiente token con:

```text
P(siguiente token | token actual)
```

Ignora todo lo anterior al token actual. Por ejemplo, produce la misma distribución después de `ba` y de `banda`, porque ambos contextos terminan en `a`.

Definí una matriz de conteos C de tamaño V × V, donde V es el tamaño del vocabulario. La fila indica el token actual y la columna indica el siguiente token:

```text
C[i, j] = cantidad de veces que el token j aparece después del token i
P[j | i] = C[i, j] / suma de la fila i
```

En este corpus, `a` tiene cinco sucesores observados: cuatro son `n` y uno es un espacio. Por lo tanto:

```text
P(n | a) = 4/5
P(espacio | a) = 1/5
```

Contar y normalizar estima las probabilidades directamente. Todavía no estamos entrenando una red neuronal.

## Ejercicio en Python

Implementá estas operaciones con la biblioteca estándar:

1. Construí el vocabulario con `sorted(set(texto))` y los mapas token → identificador e identificador → token.
2. Convertí el texto en una lista de identificadores.
3. Creá una matriz de ceros y acumulá las parejas consecutivas con `zip(ids, ids[1:])`.
4. Normalizá cada fila para obtener probabilidades. Si una fila no tiene observaciones, usá una distribución uniforme y marcala como un caso sin evidencia.
5. Mostrá la distribución correspondiente a `a`.

Comprobá que la matriz contiene 13 observaciones, que cada fila de probabilidades suma aproximadamente 1 y que la fila de `a` coincide con el ejemplo.

Antes de continuar, explicá con tus palabras: ¿por qué este modelo no puede distinguir qué debería seguir después de `ba` y de `banda`? ¿Una probabilidad cero demuestra que una transición es imposible, o solo que no apareció en este texto?

El siguiente paso será medir la calidad de las predicciones con la pérdida logarítmica. Después reemplazaremos los conteos por parámetros que se ajustan mediante gradientes.
