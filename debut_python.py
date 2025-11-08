try:
    # Saisie des nombres
    nombre1 = input("Entrez le premier nombre: ")
    nombre2 = input("Entrez le deuxième nombre: ")

    # Conversion en entiers
    nombre_1 = int(nombre1)
    nombre_2 = int(nombre2)

    # Choix de l’opération
    operation = input("Entrez l'opération (+, -, *, /): ")

    # Calcul selon l’opération
    if operation == '+':
        resultat = nombre_1 + nombre_2
        print(f"{nombre1} + {nombre2} = {resultat}")

    elif operation == '-':
        resultat = nombre_1 - nombre_2
        print(f"{nombre1} - {nombre2} = {resultat}")

    elif operation == '*':
        resultat = nombre_1 * nombre_2
        print(f"{nombre1} * {nombre2} = {resultat}")

    elif operation == '/':
        if nombre_2 != 0:
            resultat = nombre_1 / nombre_2
            print(f"{nombre1} / {nombre2} = {resultat}")
        else:
            print("Erreur : division par zéro interdite.")

    else:
        print("Opération non reconnue. Veuillez utiliser +, -, * ou /.")

except ValueError:
    print("Veuillez entrer uniquement des nombres valides.")
