# operations_delete.py
from database import datos

def eliminar(indice):
    """Elimina un elemento por su índice."""
    if 0 <= indice < len(datos):
        datos.pop(indice)
        return True
    return False
