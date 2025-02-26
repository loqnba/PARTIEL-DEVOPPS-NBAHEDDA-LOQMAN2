def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    return "Erreur : division par zéro"  # Ajout d'un return en cas de division par zéro


def greet(name):
    # GREET FUNCTION
    if name == "":
        return "Hello, World!"
    return "Hello, " + name
