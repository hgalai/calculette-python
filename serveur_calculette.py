# -*-coding:Latin-1 -*

def add(x,y):
    z=x+y
    print(z)
def soust(x,y):
    z=x-y
    print(z)
def mult(x,y):
    z=x*y
    print (z)
def div(x,y):
    z=x/y
    print(z)

import socket

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    val1=msg_recu
    print("ici :"msg_recu.decode())
    print("ici :" val1)
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()



