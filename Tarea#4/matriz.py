class Matriz:

    def __init__(self, filas: int, columnas: int) -> None:
        """Crea una matriz de filas x columnas llena de ceros.
        Complejidad: O(f * c)
        """
        if filas <= 0 or columnas <= 0:
            raise ValueError("Las filas y columnas deben ser positivas")

        self._filas = filas
        self._columnas = columnas
        self._datos = [0] * (filas * columnas)

    def filas(self) -> int:
        """Devuelve la cantidad de filas.
        Complejidad: O(1)
        """
        return self._filas

    def columnas(self) -> int:
        """Devuelve la cantidad de columnas.
        Complejidad: O(1)
        """
        return self._columnas

    def _posicion(self, i: int, j: int) -> int:
        if i < 0 or i >= self._filas or j < 0 or j >= self._columnas:
            raise IndexError("Celda fuera de la matriz")
        return i * self._columnas + j

    def obtener(self, i: int, j: int):
        """Obtiene el valor de una celda.
        Complejidad: O(1)
        """
        posicion = self._posicion(i, j)
        return self._datos[posicion]

    def asignar(self, i: int, j: int, valor) -> None:
        """Asigna un valor a una celda.
        Complejidad: O(1)
        """
        posicion = self._posicion(i, j)
        self._datos[posicion] = valor

    def suma(self):
        """Devuelve la suma de todas las celdas.
        Complejidad: O(f * c)
        """
        total = 0

        for valor in self._datos:
            total += valor

        return total
