
from boulangerie import Boulangerie
from produit import Produit, Croissant, Pain

if __name__ == '__main__':
    b = Boulangerie()
    b.addProduit(Croissant())
    b.addProduit(Pain())

    c = b.get_croissant()
    print(c)
    
