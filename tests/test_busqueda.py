"""Pruebas unitarias de búsqueda de contactos."""

import pytest

from src.agenda import (
    buscar_contactos,
    contactos,
    registrar_contacto,
)


@pytest.fixture(autouse=True)
def preparar_agenda():
    """Carga contactos antes de cada prueba."""
    contactos.clear()

    registrar_contacto("Juan Pérez", "0991234567")
    registrar_contacto("Juana López", "0987654321")
    registrar_contacto("María Torres", "0976543210")

    yield

    contactos.clear()


@pytest.mark.unit
def test_buscar_contacto_exacto():
    resultado = buscar_contactos("Juan Pérez")

    assert resultado == [
        {
            "nombre": "Juan Pérez",
            "telefono": "0991234567",
        }
    ]


@pytest.mark.unit
def test_buscar_contacto_parcial():
    resultado = buscar_contactos("Juan")

    assert len(resultado) == 2
    assert resultado[0]["nombre"] == "Juan Pérez"
    assert resultado[1]["nombre"] == "Juana López"


@pytest.mark.unit
def test_busqueda_no_distingue_mayusculas():
    resultado = buscar_contactos("MARÍA")

    assert resultado == [
        {
            "nombre": "María Torres",
            "telefono": "0976543210",
        }
    ]


@pytest.mark.unit
def test_buscar_contacto_inexistente():
    assert buscar_contactos("Carlos") == []


@pytest.mark.unit
@pytest.mark.parametrize(
    "criterio",
    [
        "",
        "   ",
        12345,
        None,
    ],
)
def test_buscar_con_criterio_invalido(criterio):
    with pytest.raises(
        ValueError,
        match="Debe ingresar un nombre válido",
    ):
        buscar_contactos(criterio)