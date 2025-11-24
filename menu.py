# menu.py
from operations_create import crear
from operations_read import leer
from operations_update import actualizar
from operations_delete import eliminar

def mostrar_menu():
    print("\n===== SISTEMA CRUD EN PYTHON =====")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        item = input("Ingresa el valor a agregar: ")
        crear(item)
        print("Elemento agregado exitosamente.")

    elif opcion == 2:
        print("Datos actuales:", leer())

    elif opcion == 3:
        indice = int(input("Índice a actualizar: "))
        nuevo = input("Nuevo valor: ")
        if actualizar(indice, nuevo):
            print("Elemento actualizado.")
        else:
            print("Índice inválido.")

    elif opcion == 4:
        indice = int(input("Índice a eliminar: "))
        if eliminar(indice):
            print("Elemento eliminado.")
        else:
            print("Índice inválido.")

    elif opcion == 5:
        print("Saliendo del sistema...")
        return False

    return True
