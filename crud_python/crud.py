# CRUD EN PYTHON
# Cada función representa una operación del CRUD.
# Este archivo se creó y actualizó en cada Pull Request del flujo requerido.

datos = []

def crear(item):
    """Agrega un nuevo elemento a la lista."""
    datos.append(item)
    return True

def leer():
    """Retorna todos los elementos almacenados."""
    return datos

def actualizar(indice, nuevo_valor):
    """Actualiza un elemento en base a su índice."""
    if 0 <= indice < len(datos):
        datos[indice] = nuevo_valor
        return True
    return False

def eliminar(indice):
    """Elimina un elemento en base a su índice."""
    if 0 <= indice < len(datos):
        datos.pop(indice)
        return True
    return False

