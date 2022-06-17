import os
import socket
import errno

try:
    # Créer une socket datagramme
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#La famille d’adresses utilisées: AF_INET
                                                        #Le type de socket: SOCK_DGRAM
    # Lier à l'adresse IP et le port
    s.bind(("localhost", 9875))
    while True :
        #question5: focntion recvfrom() 
        data,adr = s.recvfrom(1024)     #taille du tampon=1024
                                        #donnée réçu= data
                                        #adresse du client= adr

        clientMsg = "Message du client: {}".format(data)
        clientIP  = "Adresse IP du client: {}".format(adr)
        print(clientMsg)
        print(clientIP)

except socket.error as error:
    if error.errno == errno.ECONNREFUSED:
        print(os.strerror(error.errno))
    else:
        raise

s.close()