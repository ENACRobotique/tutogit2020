from produit import Produit, Croissant, Chocolatine


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

    def get_chocolatine(self) -> Chocolatine | None:
        return self.getProduit(Chocolatine)

