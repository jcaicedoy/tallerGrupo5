"""Pruebas E2E de la aplicación de consola."""

import subprocess
import sys
from pathlib import Path

import pytest


RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
APP = RAIZ_PROYECTO / "app.py"


@pytest.mark.e2e
def test_flujo_completo_registrar_buscar_y_salir():
    entradas = "\n".join(
        [
            "1",
            "Juan Pérez",
            "0991234567",
            "2",
            "Juan",
            "3",
            "",
        ]
    )

    proceso = subprocess.run(
        [sys.executable, str(APP)],
        input=entradas,
        text=True,
        capture_output=True,
        cwd=RAIZ_PROYECTO,
        timeout=10,
        check=False,
    )

    assert proceso.returncode == 0
    assert "Contacto registrado: Juan Pérez - 0991234567" in proceso.stdout
    assert "Contactos encontrados:" in proceso.stdout
    assert "Juan Pérez: 0991234567" in proceso.stdout
    assert "Gracias por utilizar la agenda." in proceso.stdout


@pytest.mark.e2e
def test_flujo_registro_con_datos_invalidos():
    entradas = "\n".join(
        [
            "1",
            "Juan123",
            "0991234567",
            "3",
            "",
        ]
    )

    proceso = subprocess.run(
        [sys.executable, str(APP)],
        input=entradas,
        text=True,
        capture_output=True,
        cwd=RAIZ_PROYECTO,
        timeout=10,
        check=False,
    )

    assert proceso.returncode == 0
    assert "Error: El nombre debe contener únicamente letras y espacios." \
        in proceso.stdout
    assert "Gracias por utilizar la agenda." in proceso.stdout


@pytest.mark.e2e
def test_flujo_busqueda_sin_resultados():
    entradas = "\n".join(
        [
            "2",
            "Carlos",
            "3",
            "",
        ]
    )

    proceso = subprocess.run(
        [sys.executable, str(APP)],
        input=entradas,
        text=True,
        capture_output=True,
        cwd=RAIZ_PROYECTO,
        timeout=10,
        check=False,
    )

    assert proceso.returncode == 0
    assert "No se encontraron contactos." in proceso.stdout