from chat import Chat
from chien import Chien
from animalerie import Animalierie
from oiseau import Ouiseau


if __name__ == "__main__":
    #ici j'ai instancié la classe animalerie 
    shop = Animalierie('La belle patte')

    # j'ai créé qq chats,chiens, et oiseaux et j'ai ajouté dans le shop
    chien1= Chien('berger allmend', True, 'rex', 3, 500);
    chein2 =Chien('berger allmend', False, 'd1', 2, 200)
    chat1= Chat('Longs poils', 'Intérieur', 'Whiskers', 2, 300)
    chat2= Chat('courtes poils', 'Exterieur', 'Whiskers', 2, 100)
    oi1 = Ouiseau('Canari', True, 'Tweety', 1, 150)
    shop.ajouter_animal(chien1)
    shop.ajouter_animal(chein2)
    shop.ajouter_animal(chat1)
    shop.ajouter_animal(chat2)
    shop.ajouter_animal(oi1)
    
    #ici j'ai affiché la liste des animaux avec leurs index
    print('*******le shop contient les animaux suivante*******')
    shop.afficher_catalogues()
    #ici j'ai utilisé la variable de classe nb_animaux
    print(shop.nombre_animaux())
    #ici je vais supprimer un animall
    shop.vendre(chat2)
    #pour testrt la supp
    print('------après la vente de chat2------')
    print(shop.nombre_animaux())
    print('*******le shop contient les animaux suivante*******')
    shop.afficher_catalogues()
    print('*******statistique par type danimal*******')
    print(shop.statistique_par_type())
    #je voualais tester l'ajout et apres la stat
    chat3= Chat('courtes poils', 'Exterieur', 'Whiskers', 2, 100)
    shop.ajouter_animal(chat3)
    print('*******après lajout de chat3*******')
    print(shop.statistique_par_type())
    #test du fonction du decrire rononronne chanter et tout ca 
    print ('-----les fonctions du chat-----')
    chat1.decrire()
    chat1.parler()
    chat1.ronronner()
    print ('*********les fonctions du chient*********')
    chien1.decrire()
    chien1.parler()
    chien1.faire_la_patte()
    print ('*********les fonctions du oiseau*********')
    oi1.decrire()
    oi1.parler()
    oi1.chanter()
    
    