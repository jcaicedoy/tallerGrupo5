"""Pruebas unitarias para el registro de contactos."""

import pytest

from src.agenda import (
    contactos,
    registrar_contacto,
    validar_nombre,
    validar_telefono,
)


@pytest.fixture(autouse=True)
def limpiar_agenda():
    """Limpia los contactos antes y después de cada prueba."""
    contactos.clear()
    yield
    contactos.clear()


@pytest.mark.parametrize(
    "nombre",
    [
        "Juan",
        "Juan Pérez",
        "María Fernanda",
        "Ángel Muñoz",
    ],
)
def test_validar_nombre_correcto(nombre):
    assert validar_nombre(nombre) is True


@pytest.mark.parametrize(
    "nombre",
    [
        "",
        "   ",
        "Juan123",
        "Carlos@",
        "Andrea_01",
        12345,
        None,
    ],
)
def test_validar_nombre_incorrecto(nombre):
    assert validar_nombre(nombre) is False


@pytest.mark.parametrize(
    "telefono",
    [
        "0991234567",
        "0987654321",
        "0223456789",
    ],
)
def test_validar_telefono_correcto(telefono):
    assert validar_telefono(telefono) is True


@pytest.mark.parametrize(
    "telefono",
    [
        "",
        "099123456",
        "09912345678",
        "09912A4567",
        "099-123456",
        991234567,
        None,
    ],
)
def test_validar_telefono_incorrecto(telefono):
    assert validar_telefono(telefono) is False


def test_registrar_contacto_correctamente():
    resultado = registrar_contacto(
        "Juan Pérez",
        "0991234567",
    )

    assert resultado == {
        "nombre": "Juan Pérez",
        "telefono": "0991234567",
    }

    assert contactos["Juan Pérez"] == "0991234567"


def test_registrar_contacto_elimina_espacios_externos():
    resultado = registrar_contacto(
        "  María López  ",
        "0987654321",
    )

    assert resultado["nombre"] == "María López"
    assert contactos["María López"] == "0987654321"


def test_registrar_contacto_con_nombre_incorrecto():
    with pytest.raises(
        ValueError,
        match="El nombre debe contener únicamente letras y espacios",
    ):
        registrar_contacto(
            "Juan123",
            "0991234567",
        )


def test_registrar_contacto_con_telefono_incorrecto():
    with pytest.raises(
        ValueError,
        match="El teléfono debe contener exactamente 10 dígitos",
    ):
        registrar_contacto(
            "Juan Pérez",
            "099123456",
        )