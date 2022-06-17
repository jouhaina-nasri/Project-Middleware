import getopt
import socket
import sys
#python3 Client.py -l effy -f effy

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("localhost", 7979))
print("Connexion ...")
login = None
host = None
argv = sys.argv[1:]
#récupère les arguments en entrée de l'exécution
opts, args = getopt.getopt(argv, "f:l:")#getopt: récupère les arguments sous la forme d'une liste
for opt, arg in opts:
    if opt in ['-f']:
        login = arg
    elif opt in ['-l']:
        host = arg
print("login = " ,login)
print("host = " , host)
if login == '':
    print("Vérifier login vide !")
    sys.exit(1)

size = 0
clientSocket.send(str.encode(login))
maxSize = int(clientSocket.recv(10000).decode())
clientSocket.send(str.encode("ok"))

while size < maxSize:
    print(str(clientSocket.recv(1024).decode()))
    size += 1024

