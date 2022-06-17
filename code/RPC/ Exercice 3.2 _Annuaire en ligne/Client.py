import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8089/")

ans=True
try:
 while ans :
 
   #---------------Menu---------------------#
   print("Choix de l’action a effectuer :")
   print("1: Ajouter une entree dans le repertoire")
   print("2: Afficher le numero de telephone d’une personne")
   print("3: Afficher le nombre de numeros enregistres dans le repertoire")
   print("4: Afficher le contenu de tout le repertoire")
   print("5: Supprimer du repertoire une personne et son numero")
   print("6: Effacer tout le contenu du repertoire")
   print("0: Quitter le programme")
   
   #---------------Choix---------------------#
   Operation=input("Choissir l'opération : ") #Saisir votre choix
   Operation=int(Operation) #Cast choix 

   #------Choix1 : Ajouter un Entree -------#
   if Operation==1 :
        Nom = input("Entrez le nom de la personne que vous enregistrez dans l'annuaire ") #Saisir votre Nom
        Telephone = input("Entrez le numéro de téléphone de la personne " ) #Saisir votre téléphone
        print(proxy.ajouterEntree(Nom, Telephone)) #Appel à la fonction ajouterEntree
 
   #------Choix2 : Trouver le Numéro de téléphone  -------#
   elif Operation==2 :
        nom = input("Entrez le nom de la personne que vous voulez rechercher ") #Saisir le nom 
        print(proxy.trouverNumero(nom)) #Afficher le numéro de téléphone trouvé

   #------Choix3 : Le nombre d’entrées dans le répertoire  -------#
   elif Operation==3 :
        print(proxy.nbNumeros()) #Afficher le nombre d'entrées dans le répertoire

   #------Choix4 : Afficher Le contenu du répertoire -------#
   elif Operation==4 :
        print(proxy.getAll()) #Appel à la fonction getAll() pur afficher le contenu du répertoire

   #------Choix5 : Supprimer un element -------#
   elif Operation==5 :
        nom = input("Entrez le nom de la personne que vous voulez supprimer ") #Saisir le nom
        print(proxy.supprimerEntree(nom)) #Appel à la fonction supprimerEntree pur supprimer un element du répertoire
 
   #------Choix6 : Supprimer toutes les entrées -------#
   elif Operation==6 :
        proxy.supprimerTout() #Appel à la fonction supprimerTout pur supprimer le contenu du répertoire

  #------Choix0 : Quitter le terminal -------#
   elif Operation==0 :
        print("Quitter....")
        ans=False #Quitter la boucle while

   else :
        print("Erreur de choisir....") #Autre Choix

except xmlrpc.client.Fault as err:
    print("A fault occurred")
