def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b


def maximum(*args):
    """Retourne la valeur maximale parmi les arguments fournis."""
    if not args:
        raise ValueError("Au moins un argument est requis")
    return max(args)


def format_nom(prenom, nom):
    """Formate un prénom et nom en majuscules avec la première lettre capitalisée."""
    return f"{prenom.capitalize()} {nom.upper()}"
