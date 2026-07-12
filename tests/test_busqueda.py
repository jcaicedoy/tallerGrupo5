"""Pruebas unitarias para la búsqueda de contactos."""

import pytest

from src.agenda import (
    buscar_contactos,
    contactos,
    registrar_contacto,
)


@pytest.fixture(autouse=True)
def preparar_agenda():
    """Prepara contactos antes de cada prueba."""
    contactos.clear()

    registrar_contacto("Juan Pérez", "0991234567")
    registrar_contacto("Juana López", "0987654321")
    registrar_contacto("María Torres", "0976543210")

    yield

    contactos.clear()


def test_buscar_contacto_por_nombre_exacto():
    resultado = buscar_contactos("Juan Pérez")

    assert resultado == [
        {
            "nombre": "Juan Pérez",
            "telefono": "0991234567",
        }
    ]


def test_buscar_contactos_por_coincidencia_parcial():
    resultado = buscar_contactos("Juan")

    assert len(resultado) == 2
    assert resultado[0]["nombre"] == "Juan Pérez"
    assert resultado[1]["nombre"] == "Juana López"


def test_buscar_contacto_sin_distinguir_mayusculas():
    resultado = buscar_contactos("MARÍA")

    assert resultado == [
        {
            "nombre": "María Torres",
            "telefono": "0976543210",
        }
    ]


def test_buscar_contacto_elimina_espacios_externos():
    resultado = buscar_contactos("  Juan Pérez  ")

    assert len(resultado) == 1
    assert resultado[0]["nombre"] == "Juan Pérez"


def test_buscar_contacto_inexistente():
    resultado = buscar_contactos("Carlos")

    assert resultado == []


@pytest.mark.parametrize(
    "criterio",
    [
        "",
        "   ",
        12345,
        None,
    ],
)
def test_buscar_contacto_con_criterio_invalido(criterio):
    with pytest.raises(
        ValueError,
        match="Debe ingresar un nombre válido",
    ):
        buscar_contactos(criterio)