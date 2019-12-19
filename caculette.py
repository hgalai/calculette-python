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

#print("Calculatrice")
a=input("Choisissez une opération: 'add', 'soust', 'mult', 'div' :")
b= input("donnez un premier nombre:")
b=float(b)
print(type(b))
c= input("donnez un second nombre:")
c=float(c)
if a=='add':
    add(b,c)
if a== 'soust':
    soust(b,c)
if a== 'mult':
    mult(b,c)
if a== 'div' :
    div(b,c)

