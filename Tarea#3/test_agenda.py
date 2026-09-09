import pytest

from agenda import Agenda


def test_agenda_vacia_tiene_len_cero():
    assert len(Agenda()) == 0


def test_agenda_vacia_no_contiene_nada():
    assert Agenda().contiene("Ana") is False


def test_agregar_incrementa_len():
    agenda = Agenda()
    agenda.agregar("Carlos", "3001111111")
    assert len(agenda) == 1


def test_contiene_nombre_existente():
    agenda = Agenda()
    agenda.agregar("Beatriz", "3002222222")
    assert agenda.contiene("Beatriz") is True


def test_contiene_nombre_inexistente():
    agenda = Agenda()
    agenda.agregar("Beatriz", "3002222222")
    assert agenda.contiene("David") is False


def test_telefono_de_nombre_existente():
    agenda = Agenda()
    agenda.agregar("Elena", "3003333333")
    assert agenda.telefono_de("Elena") == "3003333333"


def test_telefono_de_nombre_inexistente_lanza_keyerror():
    with pytest.raises(KeyError):
        Agenda().telefono_de("Fernando")


def test_agregar_nombre_repetido_actualiza_telefono():
    agenda = Agenda()
    agenda.agregar("Gloria", "3004444444")
    agenda.agregar("Gloria", "3005555555")
    assert len(agenda) == 1
    assert agenda.telefono_de("Gloria") == "3005555555"


def test_agregar_nombre_vacio_lanza_valueerror():
    with pytest.raises(ValueError):
        Agenda().agregar("", "3006666666")


def test_eliminar_nombre_existente():
    agenda = Agenda()
    agenda.agregar("Hugo", "3007777777")
    agenda.eliminar("Hugo")
    assert len(agenda) == 0
    assert agenda.contiene("Hugo") is False


def test_eliminar_nombre_inexistente_lanza_keyerror():
    with pytest.raises(KeyError):
        Agenda().eliminar("Ines")


def test_nombres_quedan_en_orden_alfabetico():
    agenda = Agenda()
    for nombre in ["Marta", "Andres", "Zoe"]:
        agenda.agregar(nombre, "1")
    assert agenda.nombres() == ["Andres", "Marta", "Zoe"]


def test_nombres_devuelve_una_copia_independiente():
    agenda = Agenda()
    agenda.agregar("Nora", "3008888888")
    nombres = agenda.nombres()
    nombres.append("Otro")
    assert agenda.contiene("Otro") is False
    assert len(agenda) == 1


def test_mayusculas_y_tildes_son_nombres_distintos():
    agenda = Agenda()
    agenda.agregar("ana", "1")
    agenda.agregar("Ana", "2")
    agenda.agregar("Ána", "3")
    assert agenda.nombres() == ["Ana", "ana", "Ána"]
    assert len(agenda) == 3
