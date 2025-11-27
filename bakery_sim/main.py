
from boulangerie import Boulangerie
from produit import Produit, Croissant, Pain, Chocolatine

if __name__ == '__main__':
    b = Boulangerie()
    for _ in range(10):
      b.addProduit(Croissant())
      b.addProduit(Chocolatine())
      b.addProduit(Pain())
      b.addProduit(Pain())
    


    c = b.get_croissant()

    paint_au_chocolat = b.get_chocolatine()
    print(c)
    
