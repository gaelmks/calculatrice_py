import numpy
def addition(a,b):
    return a+b
def soustraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def reste(a,b):
    return a%b

nombre1=float(input(" "))
nombre2=float(input(" "))
choix=" "
if choix=='+':
    reponse=addition(nombre1,nombre2)
    print(reponse)
elif choix=='-':
    reponse=soustraction(nombre1,nombre2)
    print(reponse)
elif choix=='*':
    reponse=multiplication(nombre1,nombre2)
    print(reponse)
elif choix=='/':
    reponse= division(nombre1,nombre2)
    print(reponse)