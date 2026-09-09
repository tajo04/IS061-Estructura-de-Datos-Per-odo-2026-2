"""TAD Agenda: contactos ordenados por nombre, sobre listas de Python."""


class Agenda:
    def __init__(self) -> None:
        """
        Crea una agenda vacía.
        Complejidad: O(1)
        """
        self._nombres: list[str] = []
        self._telefonos: list[str] = []

    def __len__(self) -> int:
        """
        Devuelve cuántos contactos hay en la agenda.
        Complejidad: O(1)
        """
        return len(self._nombres)

    def _buscar(self, nombre: str) -> tuple[bool, int]:
        """
        Búsqueda binaria interna. Devuelve una tupla (encontrado, indice):
        si el nombre está, indice es su posición; si no está, indice es
        la posición donde habría que insertarlo para mantener el orden.
        Complejidad: O(log n)
        """
        inicio = 0
        fin = len(self._nombres)
        while inicio < fin:
            medio = (inicio + fin) // 2
            actual = self._nombres[medio]
            if actual < nombre:
                inicio = medio + 1
            elif actual > nombre:
                fin = medio
            else:
                return True, medio
        return False, inicio

    def contiene(self, nombre: str) -> bool:
        """
        Indica si ese nombre está en la agenda.
        Complejidad: O(log n)
        """
        encontrado, _ = self._buscar(nombre)
        return encontrado

    def telefono_de(self, nombre: str) -> str:
        """
        Devuelve el teléfono de ese contacto. Si no está, lanza KeyError.
        Complejidad: O(log n)
        """
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        return self._telefonos[indice]

    def nombres(self) -> list[str]:
        """
        Devuelve todos los nombres, en orden alfabético, en una lista
        nueva: quien la reciba puede modificarla sin afectar la agenda.
        Complejidad: O(n)
        """
        return list(self._nombres)

    def agregar(self, nombre: str, telefono: str) -> None:
        """
        Agrega el contacto. Si el nombre ya existe, actualiza el
        teléfono en vez de duplicarlo. Si el nombre está vacío, lanza
        ValueError. El teléfono se guarda como texto (str).
        Complejidad: O(n)
        """
        if nombre == "":
            raise ValueError("el nombre no puede estar vacío")
        encontrado, indice = self._buscar(nombre)
        if encontrado:
            self._telefonos[indice] = str(telefono)
        else:
            self._nombres.insert(indice, nombre)
            self._telefonos.insert(indice, str(telefono))

    def eliminar(self, nombre: str) -> None:
        """
        Elimina ese contacto. Si no está, lanza KeyError.
        Complejidad: O(n)
        """
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        del self._nombres[indice]
        del self._telefonos[indice]
