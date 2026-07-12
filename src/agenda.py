"""Funciones principales de la agenda telefónica."""

contactos: dict[str, str] = {}


def validar_nombre(nombre: str) -> bool:
    """
    Verifica que el nombre contenga únicamente letras y espacios.

    Args:
        nombre: Nombre del contacto que se desea validar.

    Returns:
        True cuando el nombre es válido; False en caso contrario.
    """
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
    """
    Verifica que el teléfono tenga exactamente diez dígitos.

    Args:
        telefono: Número telefónico que se desea validar.

    Returns:
        True cuando el teléfono es válido; False en caso contrario.
    """
    if not isinstance(telefono, str):
        return False

    return len(telefono) == 10 and telefono.isdigit()


def registrar_contacto(nombre: str, telefono: str) -> dict[str, str]:
    """
    Registra un contacto después de validar su nombre y teléfono.

    Args:
        nombre: Nombre del contacto.
        telefono: Número telefónico de diez dígitos.

    Returns:
        Diccionario con el nombre y teléfono registrados.

    Raises:
        ValueError: Si el nombre o el teléfono no son válidos.
    """
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