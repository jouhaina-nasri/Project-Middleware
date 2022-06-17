from xmlrpc.server import SimpleXMLRPCServer

class Calcul:

    #Fonction Addition
    def add(x, y):
        try:
            return x+y
        except TypeError:
            print("Merci d'utiliser des chiffres")
            return None

   #Fonction multiplication
    def mult(x, y):
        try:
            return x*y
        except TypeError:
            print("Merci d'utiliser des chiffres")
            return None
    
    #Fonction Différence
    def diff(x, y):
        try:
            return x-y
        except TypeError:
            print("Merci d'utiliser des chiffres")
            return None
    
    #Fonction quotient
    def quotient(x, y):
        try:
            return x/y
        except TypeError:
            print("Merci d'utiliser des chiffres")
            return None
        except ZeroDivisionError:
            print("Merci de ne pas diviser par 0")
            return None
    
    #Fonction Absolue
    def absolue(x):
        try:
            return abs(x)
        except TypeError:
            print("Merci d'utiliser des chiffres")
            return None
    


server = SimpleXMLRPCServer(("localhost", 8085))

print("Serveur en écoute")

server.register_function(Calcul.add, 'add')
server.register_function(Calcul.mult, 'mult')
server.register_function(Calcul.diff, 'diff')
server.register_function(Calcul.quotient, 'quotient')
server.register_function(Calcul.absolue, 'absolue')

server.serve_forever()