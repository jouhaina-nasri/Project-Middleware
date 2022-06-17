import os
import socket
import errno


try:
    # Créer une socket TCP
    ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #La famille d’adresses utilisées: AF_INET
                                                                #Le type de socket: SOCK_STREAM

    # Lier à l'adresse IP et le port
    ssocket.bind(("localhost", 8016))


    # On passe la socket en mode écoute
    ssocket.listen()
    
    #question13: fonction accept()
    while True: 
        s_service, adr = ssocket.accept()
        data = s_service.recv(1024)
        if (len(data)== 0): #Si le serveur a reçu un message de longueur nulle
            s_service.close()
            break

        # Envoyer Ok au client 
        msg = str.encode("OK")
        s_service.send(msg)

        #Afficher le msg réçu du client
        clientMsg = "Message du client: {}".format(data)
        print(clientMsg)

except socket.error as error:
    if error.errno == errno.ECONNREFUSED:
        print(os.strerror(error.errno))
    else:
        raise


ssocket.close()
