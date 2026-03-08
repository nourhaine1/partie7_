from animal import Animal

class Ouiseau(Animal):
    def __init__(self,espece,peut_voler,nom,age,prix):
        super().__init__(nom,age,prix);
        self.espece = espece;
        self.peut_voler = peut_voler
    
    def parler(self):
        print('le ouiseau vizviz')
    def decrire(self):
        print(f'le ouiseau est appelé {self.nom},son age est {self.age} son prix est {self.prix} appartient à l espece {self.espece} et il peut voler {self.peut_voler}')
    def chanter(self):
        print (f'le ouiseau  appartient à l espece {self.espece} et il peut voler {self.peut_voler}')