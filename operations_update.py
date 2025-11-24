# operations_update.py
from database import datos

def actualizar(indice, nuevo_valor):
    """Actualiza un valor por su índice."""
    if 0 <= indice < len(datos):
        datos[indice] = nuevo_valor
        return True
    return False
