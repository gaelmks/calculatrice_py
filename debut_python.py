nombre1 = input("Entrez le premier nombre: ")
nombre2 = input("Entrez le deuxième nombre: ")
resultat = int
if nombre1.isnumeric() and nombre2.isnumeric():
   nombre_1 = int(nombre1)
   nombre_2 = int(nombre2)
else:
   print("Veuillez entrer des nombres valides.") 
 
operation = input("Entrez l'opération (+, -, *, /): ")
if operation == '+':
    resultat = nombre_1 + nombre_2
    print(f"{nombre1} + {nombre2} le résultalt est: {resultat}")

elif operation == '/':
   if nombre_2 !=0:
      resultat = nombre_1 / nombre_2
      print(f"{nombre1} / {nombre2} le résultalt est: {resultat}")
elif operation == '-':
    resultat = nombre_1 - nombre_2
    print(f"{nombre1} - {nombre2} le résultalt est: {resultat}")
elif operation == '*':
    resultat = nombre_1 * nombre_2
    print(f"{nombre1} * {nombre2} le résultalt est: {resultat}")

else:
    print("Opération non reconnue. Veuillez utiliser +, -, * ou /.")