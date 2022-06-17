import socket 

msgClient = "Salut Serveur, je suis un client UDP"
msgToSend = str.encode(msgClient)

addrPort = ("localhost", 9875)
# Créer un socket UDP coté client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Envoyer au serveur à l'aide du socket UDP créé
s.sendto(msgToSend, addrPort)

s.close()
