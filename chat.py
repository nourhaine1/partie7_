from animal import Animal

class Chat(Animal):
    def __init__(self,longeur_pols,interieur,nom,age,prix):
        super().__init__(nom,age,prix);
        self.longeur_pols = longeur_pols;
        self.interieur = interieur;
       
    
    def parler(self):
        print('le chat miaule')
    def decrire(self):
        print(f'le chat est appelé {self.nom},son age est {self.age} son prix est {self.prix} ses poils sont  {self.longeur_pols} et il est {self.interieur}')
    def ronronner(self):
        print (f'le chat {self.nom} ronronne')