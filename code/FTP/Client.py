import socket

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip ="localhost"
port=6662
s.connect((ip, port))
print ("Connexion avec succès")

choix=input("Pour un transfert du client vers le serveur entrez 1 sinon 2 pour un transfert du serveur vers le client\n")

if choix == "1":
         s.send(bytes("Client to serveur",'UTF-8'))
         filetosend = open("filecs.txt","r+")#Le mode r+ permet d’ouvrir un fichier en lecture et en écriture
         try:
            data = filetosend.read(1024)
         except:
            print("Problème dans la lecture de data")

         while data:
            print("Envoi...")
            data=data.encode()
            s.send(data)

            data = filetosend.read(1024)
      
         filetosend.close()
         print("Envoi terminé avec succès.")
      
         s.shutdown(2)
         s.close()
elif choix == "2":
        s.send(bytes("serveur to client",'UTF-8'))  
        data = s.recv(BUFFER_SIZE)
        print("msg du Serveur :" , data.decode())
        s.send(bytes("Connexion avec succes!!",'UTF-8'))
        filetodown = open("filesc.txt", "w")
        filetodown.write(data.decode())    
        filetodown.close()
        s.close()
else:
        print ("Choix invalide")
        s.close()
  
