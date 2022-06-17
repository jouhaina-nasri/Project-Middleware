import os
import socket
import errno
import time


try:
    # Créer une socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #La famille d’adresses utilisées: AF_INET
                                                        #Le type de socket: SOCK_STREAM

    s.connect(("localhost", 8016))

    #time.sleep(3)#question 19: bloquer le client pendant 3 sec
    
    #récupérer le nom du machine pour l'envoyer au serveur
    host=socket.gethostname()
    print(host)
    msgToSend = str.encode(host)
    print(msgToSend)

    #le client a envoyé son nom de machine au serveur
    s.send(msgToSend)


    #le client a reçu un msg 
    msg = s.recv(1024)

    #Afficher le message réçu du serveur
    serveurMsg = "Message du serveur: {}".format(msg)
    print(serveurMsg)





except socket.error as error:
    if error.errno == errno.ECONNREFUSED:
        print(os.strerror(error.errno))
    else:
        raise

s.close()