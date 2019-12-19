# -*-coding:Latin-1 -*
# -*-coding:utf-8 -*
def add(x,y):
    z=x+y
    print("le résultat est: ",z)
def soust(x,y):
    z=x-y
    print("le résultat est: ",z)
def mult(x,y):
    z=x*y
    print ("le résultat est: ",z)
def div(x,y):
    z=x/y
    print("le résultat est: ",z)

print("Calculatrice")
a=input("Choisissez une opération: 'add', 'soust', 'mult', 'div' :")
b= float(input("donnez un premier nombre:"))
c= float(input("donnez un second nombre:"))
if a=='add':
    add(b,c)
if a=='soust':
    soust(b,c)
if a=='mult':
    mult(b,c)
if a=='div' :
    div(b,c)

