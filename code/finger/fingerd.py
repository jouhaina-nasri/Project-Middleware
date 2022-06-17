import datetime
import errno
import os
import socket
import subprocess
from os import getpid

#fonction qui écrit le pid du processus en cours dans un fichier
def writeinFinger():
    f = open("/tmp/finger.pid", "w")
    pid = getpid()
    f.write(str(pid))
    f.close()

try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind(("localhost", 7979))
            serverSocket.listen()
            print("Serveur en écoute...")

            print("Ecriture du process id dans le fichier ...")
            writeinFinger()

            #fonction accepte qui accepte tous les cnx et retourne socket du client et son adresse
            (client, adrr) = serverSocket.accept()

            login = client.recv(1024).decode()#récupérer login 

            concat = "finger" + ' ' + login #concaténation du "finger" avec la chaîne de caractères reçus(login)
            out = subprocess.getoutput(concat)#résultat du cmd finger
                                                #le module commands n'exist plus en python3 
                                                #il est donc remplacé par celui du subprocess
        
            tailleMax = len(str.encode(out))
            client.send(str.encode(str(tailleMax)))
            client.recv(1024)
            size = 0
            end = 1024
            while size < tailleMax:
                client.send(str.encode(out[size:end]))
                size += 1024
                end = end + 1024
            s = open("/tmp/finger.log", "r+")#ouvrir le fichier "/tmp/finger.log"
            s.write(str(datetime.datetime.now()))
            s.write(" : ")
            s.write(login)
            s.write(str(adrr[0]))
            s.write(str(adrr[1]))
            s.write("\n")
            s.close()
except socket.error as error:
    if error.errno == errno.ECONNREFUSED:
        print(os.strerror(error.errno))
    else:
        raise
    
serverSocket.close()
