

class Produit:
    
    def getName() -> str:
        raise Exception("Unimplemented!")
    
    def getIngredients() -> list[str]:
        raise Exception("Unimplemented!")


class Croissant(Produit):
    def __init__(self):
        pass

    def getName():
        return "Croissant"

    def getIngredients():
        return ["beurre", "sucre", "farine", "oeuf", "levure"]


class Pain(Produit):
    def __init__(self):
        pass
