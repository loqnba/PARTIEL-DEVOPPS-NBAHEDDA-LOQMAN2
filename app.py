def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    beta = 0  # Cette variable n'est pas utilisée, tu peux la supprimer si inutile
    if y != 0:
        return x / y


def greet(name):
    # GREET FUNCTION
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name

