from abc import ABC, abstractmethod

class Animal(ABC):
    
    nb_animaux = 0
    
    def __init__(self,nom,age,prix):
        self.nom = nom;
        self.age = age;
        self.__prix = prix ;
        Animal.nb_animaux +=1
        
    @abstractmethod    
    def parler(self):
        pass
    @abstractmethod    

    def decrire(self):
        pass

    def vendre(self):
        print(f'le prix de vente est {self.__prix}')
    
    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self,p):
        if(p>0):
            self.__prix = p
            print(f'le prix est :{self.__prix}')
        else:
            print('le prix ne doit pas null')
    def __str__(self):
        return f'Animal est {self.nom}, son age est {self.age} et son prix est {self.__prix}'    
    
    
        
        
        
        
    