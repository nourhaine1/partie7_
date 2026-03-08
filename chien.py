
from animal import Animal
class Chien(Animal):
    def __init__(self,race,est_dresse,nom,age,prix):
        super().__init__(nom,age,prix);
        self.race = race;
        self.est_dresse = est_dresse
    
    def parler(self):
        print('le chien aboie')
    def decrire(self):
        print(f'le chien est appelé {self.nom},son age est {self.age} son prix est {self.prix} appartient à la race {self.race} et il est {self.est_dresse}')
    def faire_la_patte(self):
        print (f'le chien  appartient à la race {self.race} et il est {self.est_dresse}')