# main.py
from menu import mostrar_menu, ejecutar_opcion

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            continuar = ejecutar_opcion(opcion)
        except ValueError:
            print("Debes ingresar un número válido.")

if __name__ == "__main__":
    main()
