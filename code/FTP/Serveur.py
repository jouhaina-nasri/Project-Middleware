import socket

BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6662))# Lier à l'adresse IP et le port
server.listen()
print("Serveur en attente")
conn,clientAddress = server.accept()
   
    
choix=conn.recv(1024)
    
if choix == b"Client to serveur":

            data = conn.recv(BUFFER_SIZE)
            print("Message du Client : " , data.decode())

            conn.send(bytes("Connexion avec succes!",'UTF-8'))

            filetodown = open("cs.txt", "w")
            filetodown.write(data.decode())    
            filetodown.close()

            conn.close()


elif choix == b"serveur to client":
            filetosend = open("sc.txt","r+")
            try:
                data = filetosend.read(1024)
            except:
                print("problème dans la lecture de data")

            while data:
                print("Envoi...")
                data=data.encode()
                conn.send(data)
                data = filetosend.read(1024)
            
            filetosend.close()
            print("Envoi terminé avec succès.")
            
            conn.shutdown(2)
            conn.close()
        

conn.close()
server.close()