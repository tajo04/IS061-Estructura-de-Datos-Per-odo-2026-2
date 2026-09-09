""

import random
import string
import time

from agenda import Agenda

REPETICIONES = 5


def generar_nombres(cantidad: int) -> list[str]:
    nombres: set[str] = set()
    while len(nombres) < cantidad:
        nombre = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
        nombres.add(nombre)
    return list(nombres)


def mejor_tiempo(funcion, repeticiones: int = REPETICIONES) -> float:
    mejor = float("inf")
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        mejor = min(mejor, time.perf_counter() - inicio)
    return mejor


def medir_agenda(cantidad: int) -> dict:
    agenda = Agenda()
    for nombre in generar_nombres(cantidad):
        agenda.agregar(nombre, "3000000000")

    nombre_ausente = "ZZZZZZZZZZ"

    t_binaria = mejor_tiempo(lambda: agenda.contiene(nombre_ausente))

    lista_nombres = agenda.nombres()

    def busqueda_ingenua() -> bool:
        for nombre in lista_nombres:
            if nombre == nombre_ausente:
                return True
        return False

    t_ingenua = mejor_tiempo(busqueda_ingenua)

    nombre_primero = "AAAAAAAAAA"

    def agregar_y_eliminar() -> None:
        agenda.agregar(nombre_primero, "1111111111")
        agenda.eliminar(nombre_primero)

    t_agregar = mejor_tiempo(agregar_y_eliminar)

    return {
        "cantidad": cantidad,
        "binaria": t_binaria,
        "ingenua": t_ingenua,
        "agregar": t_agregar,
    }


def formatear_numero(valor: int) -> str:
    return f"{valor:,}".replace(",", ".")


def formatear_microsegundos(segundos: float) -> str:
    microsegundos = segundos * 1_000_000
    return f"{microsegundos:.2f}".replace(".", ",")


def main() -> None:
    random.seed(11)
    tamanos = [1_000, 10_000, 100_000]
    resultados = [medir_agenda(n) for n in tamanos]

    encabezado = f"{'Contactos':>12} | {'Binaria (µs)':>13} | {'Ingenua (µs)':>13} | {'Agregar+Eliminar (µs)':>22}"
    print(encabezado)
    print("-" * len(encabezado))
    for r in resultados:
        print(
            f"{formatear_numero(r['cantidad']):>12} | "
            f"{formatear_microsegundos(r['binaria']):>13} | "
            f"{formatear_microsegundos(r['ingenua']):>13} | "
            f"{formatear_microsegundos(r['agregar']):>22}"
        )


if __name__ == "__main__":
    main()
