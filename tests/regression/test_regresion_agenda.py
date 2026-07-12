"""Pruebas de regresión de la agenda telefónica."""

import pytest

from src.agenda import (
    buscar_contactos,
    contactos,
    registrar_contacto,
)


@pytest.fixture(autouse=True)
def limpiar_agenda():
    contactos.clear()
    yield
    contactos.clear()


@pytest.mark.regression
def test_registro_sigue_funcionando_despues_de_agregar_busqueda():
    contacto = registrar_contacto(
        "Ana Gómez",
        "0991112233",
    )

    assert contacto["nombre"] == "Ana Gómez"
    assert contacto["telefono"] == "0991112233"


@pytest.mark.regression
def test_varios_contactos_no_se_sobrescriben():
    registrar_contacto("Ana Gómez", "0991112233")
    registrar_contacto("Luis Pérez", "0982223344")

    assert len(contactos) == 2
    assert contactos["Ana Gómez"] == "0991112233"
    assert contactos["Luis Pérez"] == "0982223344"


@pytest.mark.regression
def test_busqueda_no_modifica_contactos_registrados():
    registrar_contacto("Ana Gómez", "0991112233")
    registrar_contacto("Ana Torres", "0982223344")

    cantidad_inicial = len(contactos)

    resultados = buscar_contactos("Ana")

    assert len(resultados) == 2
    assert len(contactos) == cantidad_inicial


@pytest.mark.regression
def test_error_de_registro_no_guarda_informacion_invalida():
    with pytest.raises(ValueError):
        registrar_contacto("Ana123", "0991112233")

    assert contactos == {}


@pytest.mark.regression
def test_busqueda_inexistente_no_elimina_contactos():
    registrar_contacto("Ana Gómez", "0991112233")

    resultado = buscar_contactos("Carlos")

    assert resultado == []
    assert contactos["Ana Gómez"] == "0991112233"