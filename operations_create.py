# operations_create.py
from database import datos

def crear(item):
    """Agrega un nuevo elemento a la lista."""
    datos.append(item)
    return True
