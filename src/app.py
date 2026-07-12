"""Aplicación de consola para gestionar una agenda telefónica."""

from src.agenda import buscar_contactos, registrar_contacto


def mostrar_menu() -> None:
    """Muestra las opciones disponibles."""
    print("\n=== AGENDA TELEFÓNICA ===")
    print("1. Registrar contacto")
    print("2. Buscar contacto")
    print("3. Salir")


def opcion_registrar() -> None:
    """Solicita los datos y registra un contacto."""
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")

    try:
        contacto = registrar_contacto(nombre, telefono)
        print(
            f"Contacto registrado: "
            f"{contacto['nombre']} - {contacto['telefono']}"
        )
    except ValueError as error:
        print(f"Error: {error}")


def opcion_buscar() -> None:
    """Solicita un criterio y muestra los contactos encontrados."""
    nombre = input("Ingrese el nombre a buscar: ")

    try:
        resultados = buscar_contactos(nombre)

        if not resultados:
            print("No se encontraron contactos.")
            return

        print("Contactos encontrados:")

        for contacto in resultados:
            print(f"- {contacto['nombre']}: {contacto['telefono']}")

    except ValueError as error:
        print(f"Error: {error}")


def ejecutar_aplicacion() -> None:
    """Ejecuta el menú principal de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_registrar()
        elif opcion == "2":
            opcion_buscar()
        elif opcion == "3":
            print("Gracias por utilizar la agenda.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_aplicacion()