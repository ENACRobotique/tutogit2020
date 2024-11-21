from produit import Produit, Croissant, Pain


class Boulangerie:
    def __init__(self):
        self.produits: list[Produit] = []
    
    def addProduit(self, produit: Produit):
        self.produits.append(produit)
    
    def getProduit(self, productClass):
        produit = None
        for i, p in enumerate(self.produits):
            if isinstance(p, productClass):
                produit = self.produits.pop(i)
                break
        return produit
    
    def get_croissant(self) -> Croissant | None:
        return self.getProduit(Croissant)

    def get_pain(self) -> Pain | None:
        return self.getProduit(Pain)


