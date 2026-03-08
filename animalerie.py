from animal import Animal


class Animalierie:
    
    def __init__(self,nom):
        self.__nom = nom;
        self.__animaux = [];
        
        
    def ajouter_animal(self,animal):
        self.__animaux.append(animal);
        
    def afficher_animaux(self):
        for animal in self.__animaux:
            print(animal);
            
    def nombre_animaux (self):
        return Animal.nb_animaux
    
    def afficher_catalogues(self):
        for index, animal in enumerate(self.__animaux):
               print(f"{index} : {animal}")
    
    def rechereche_par_type(self,type_animal):
        for animal in self.__animaux:
            if isinstance(animal,type_animal):
                print(animal)
                
                
    def statistique_par_type(self):
        statistiques = {}
        for animal in self.__animaux:
            type_animal = type(animal).__name__
            if type_animal in statistiques:
                statistiques[type_animal] += 1
            else:
                statistiques[type_animal] = 1
        return statistiques     
      
    def vendre(self,animal):
        self.__animaux.remove(animal)
        Animal.nb_animaux -= 1

            