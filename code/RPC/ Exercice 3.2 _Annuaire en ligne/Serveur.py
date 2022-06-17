from xmlrpc.server import SimpleXMLRPCServer
i=0

class Annuaire:
    #La fonction ajouterEntree
    def ajouterEntree(Nom, NumeroDeTelephone):
        global i #declarer i comme une variable globale
        i += 1   #Avancer le compteur
        Repertoire=open("Repertoire.txt", 'a') #Ouvrir le fichier Repertoire.txt
        Repertoire.write("['"+Nom+"'"+" "+"'"+NumeroDeTelephone+"']"+"\n") #Ajouter un nom et un numero de telephone
        Repertoire.close #Fermer le fichier Repertoire.txt
        return "Element ajouté"

    #La fonction trouverNumero
    def trouverNumero(nom):
        global i #declarer i comme une variable globale
        i += 1    #Avancer le compteur
        Repertoire=open("Repertoire.txt") #Ouvrir le fichier Repertoire.txt
        ligne=Repertoire.readlines()
        for l in ligne:
            if nom in l:
                annuaire=[] 
                l=l.replace("\n","")
                l=l.replace("']","")
                l=l.replace("'","")
                l=l.split()
                annuaire.append(l)
                for elem in annuaire:
                    return elem[1]
                    
   #La fonction trouverNumero
    def nbNumeros():
        global i
        return i #retourne le nombre d’entrées dans le répertoire 
    

   #La fonction getAll
    def getAll():
        global i
        i += 1 #Avancer le compteur
        Repertoire=open("Repertoire.txt",'r') #Ouvrir le fichier Repertoire.txt
        text=Repertoire.read()
        return text

    
   #La fonction supprimeEntree
    def supprimerEntree(nom):
        global i
        i += 1 #Avancer le compteur
        with open("Repertoire.txt","r+") as f:
            nv_fichier = f.readlines()
            f.seek(0)
            for line in nv_fichier:
                if nom not in line:
                    f.write(line)
            f.truncate()
            return "supprimé avec succés"          
 
   #La fonction supprimerTout()
    def supprimerTout():
        global i
        i += 1 #Avancer le compteur
        with open("Repertoire.txt",'r+') as f:
            f.truncate(0)

    
server = SimpleXMLRPCServer(("localhost", 8089))

print("Serveur en écoute")

server.register_function(Annuaire.ajouterEntree, 'ajouterEntree')
server.register_function(Annuaire.trouverNumero, 'trouverNumero')
server.register_function(Annuaire.nbNumeros, 'nbNumeros')
server.register_function(Annuaire.getAll, 'getAll')
server.register_function(Annuaire.supprimerEntree, 'supprimerEntree')
server.register_function(Annuaire.supprimerTout, 'supprimerTout')

server.serve_forever()