from dataclasses import dataclass


@dataclass(frozen=True)
class Contacto:

    nombre: str
    telefono: str


class Agenda:

    def __init__(self) -> None:

        self._contactos: list[Contacto] = []

    def __len__(self) -> int:

        return len(self._contactos)

    def _buscar(self, nombre: str) -> tuple[bool, int]:
        inicio = 0
        fin = len(self._contactos)
        while inicio < fin:
            medio = (inicio + fin) // 2
            actual = self._contactos[medio].nombre
            if actual < nombre:
                inicio = medio + 1
            elif actual > nombre:
                fin = medio
            else:
                return True, medio
        return False, inicio

    def contiene(self, nombre: str) -> bool:

        encontrado, _ = self._buscar(nombre)
        return encontrado

    def telefono_de(self, nombre: str) -> str:
  
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        return self._contactos[indice].telefono

    def nombres(self) -> list[str]:
    
        return [contacto.nombre for contacto in self._contactos]

    def agregar(self, nombre: str, telefono: str) -> None:
      
        if nombre == "":
            raise ValueError("el nombre no puede estar vacío")
        encontrado, indice = self._buscar(nombre)
        telefono_texto = str(telefono)
        if encontrado:
            self._contactos[indice] = Contacto(nombre, telefono_texto)
        else:
            self._contactos.insert(indice, Contacto(nombre, telefono_texto))

    def eliminar(self, nombre: str) -> None:
      
        encontrado, indice = self._buscar(nombre)
        if not encontrado:
            raise KeyError(nombre)
        self._contactos.pop(indice)
