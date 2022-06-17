import xmlrpc.client

try:
 proxy = xmlrpc.client.ServerProxy("http://localhost:8085/")

 ans=True #variable pour entrer dans la boucle while

 while ans and proxy:


   
   # Afficher Menu
   print("-----Menu Calculatrice-----")
   print("1- Additon")
   print("2- Multiplication")
   print("3- Différence")
   print("4- Quotient")
   print("5- Absolue")
   print("0- Exit")
   print("---------------------------")
   
   Operation=input("Choissir l'opération : ") #Saisir le choix de l'operation
   
   try : 
        Operation=int(Operation)
   
        if Operation<5 and Operation>0:

                x=float(input("Entrer valeur x ")) #Saisir valeur1
                y=float(input("Entrer valeur y ")) #Saisir valeur2
         
         
                if Operation==1 :
                    print("Résultat de l'addition est : ")
                    print( proxy.add(x,y))


                elif Operation==2 :
                    print("Résultat de la multiplication est : ")
                    print( proxy.mult(x,y))


                elif Operation==3 :
                    print("Résultat de la différence est : ")
                    choix=input("Si X-Y entrez 1 Si Y-X entrez 2")
                    if choix=="x":
                        print( proxy.diff(x,y))
                    elif choix=="y":
                        print( proxy.diff(y,x))
                    else :
                        print("erreur")


                elif Operation==4 :
                    print("Résultat de la quotient est : ")
                    choix=input("Si X\Y entrez 1 Si Y\X entrez 2")
                    if choix=="1":
                        print( proxy.quotient(x,y))
                    elif choix=="2":
                        print( proxy.quotient(y,x))
                    else :
                        print("erreur")


                

        elif Operation==5 :
                    x=float(input("Entrer valeur 1 "))
                     
                    print("Résultat de la valeur absolue du x est : ")
                    print( proxy.absolue(x))

        elif Operation==0 :
                print("Quitter....")
                ans=False


        else :
                print("Erreur de choisir....")

   except :
      print("Veuillez insérer un chiffre valide")

except xmlrpc.client.Fault as err:
    print("Fault code: %d" % err.faultCode)
    print("Fault string: %s" % err.faultString)
    