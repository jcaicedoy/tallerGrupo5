"""Lógica principal de la agenda telefónica."""

contactos: dict[str, str] = {}


def validar_nombre(nombre: str) -> bool:
    """Valida que el nombre tenga únicamente letras y espacios."""
    if not isinstance(nombre, str):
        return False

    nombre_limpio = nombre.strip()

    if not nombre_limpio:
        return False

    return all(
        caracter.isalpha() or caracter.isspace()
        for caracter in nombre_limpio
    )


def validar_telefono(telefono: str) -> bool:
    """Valida que el teléfono tenga exactamente diez dígitos."""
    if not isinstance(telefono, str):
        return False

    return len(telefono) == 10 and telefono.isdigit()


def registrar_contacto(nombre: str, telefono: str) -> dict[str, str]:
    """Registra un contacto después de validar sus datos."""
    nombre_limpio = nombre.strip() if isinstance(nombre, str) else nombre

    if not validar_nombre(nombre_limpio):
        raise ValueError(
            "El nombre debe contener únicamente letras y espacios."
        )

    if not validar_telefono(telefono):
        raise ValueError(
            "El teléfono debe contener exactamente 10 dígitos."
        )

    contactos[nombre_limpio] = telefono

    return {
        "nombre": nombre_limpio,
        "telefono": telefono,
    }


def buscar_contactos(nombre: str) -> list[dict[str, str]]:
    """Busca contactos por coincidencia parcial del nombre."""
    if not isinstance(nombre, str) or not nombre.strip():
        raise ValueError(
            "Debe ingresar un nombre válido para realizar la búsqueda."
        )

    criterio = nombre.strip().casefold()
    resultados: list[dict[str, str]] = []

    for nombre_contacto, telefono in contactos.items():
        if criterio in nombre_contacto.casefold():
            resultados.append(
                {
                    "nombre": nombre_contacto,
                    "telefono": telefono,
                }
            )

    return resultados