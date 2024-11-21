

class Produit:
    
    def getName() -> str:
        raise Exception("Unimplemented!")
    
    def getIngredients() -> list[str]:
        raise Exception("Unimplemented!")


class Croissant(Produit):
    def __init__(self):
        pass

    def getName(self):
        return "Croissant"

    def getIngredients(self):
        return ["beurre", "sucre", "farine", "oeuf", "levure"]


class Pain(Produit):
    def __init__(self):
        pass

    def getName(self):
        return "Pain"

    def getIngredients(self):
        return ["farine","levure","eau","sel"]

class Haha(Produit):
    def __init__(self):
        pass

    def getName(self):
        return "HAHA"