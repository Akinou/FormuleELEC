# Demander à l'utilisateur quelle grandeur électrique il souhaite calculer
print("Quelle grandeur électrique voulez-vous calculer ?")
print("1 - Tension")
print("2 - Puissance")
print("3 - Intensité")
print("4 - Énergie")
print("5 - Fréquence")
print("6 - Résistance")
print("7 - Impédance")
print("8 - Réactance")
print("9 - Impédance complexe")
choix = input("Entrez le numéro correspondant à la grandeur électrique souhaitée : ")
# Calculer la grandeur électrique en fonction du choix de l'utilisateur
if choix == "1":
    # Calcul de la tension
    P = float(input("Entrez la puissance en watts : "))
    I = float(input("Entrez l'intensité en ampères : "))
    U = P / I
    print("La tension est de", U, "volts.")
    
elif choix == "2":
    # Calcul de la puissance
    U = float(input("Entrez la tension en volts : "))
    I = float(input("Entrez l'intensité en ampères : "))
    P = U * I
    print("La puissance est de", P, "watts.")
    
elif choix == "3":
    # Calcul de l'intensité
    U = float(input("Entrez la tension en volts : "))
    P = float(input("Entrez la puissance en watts : "))
    I = P / U
    print("L'intensité est de", I, "ampères.")
    
elif choix == "4":
    # Calcul de l'énergie
    P = float(input("Entrez la puissance en watts : "))
    t = float(input("Entrez le temps en secondes : "))
    E = P * t
    print("L'énergie est de", E, "joules.")
    
elif choix == "5":
    # Calcul de la fréquence
    T = float(input("Entrez la période en secondes : "))
    f = 1 / T
    print("La fréquence est de", f, "hertz.")
    
elif choix == "6":
    # Calcul de la résistance
    U = float(input("Entrez la tension en volts : "))
    I = float(input("Entrez l'intensité en ampères : "))
    R = U / I
    print("La résistance est de", R, "ohms.")
    
elif choix == "7":
    # Calcul de l'impédance
    U = float(input("Entrez la tension en volts : "))
    I = float(input("Entrez l'intensité en ampères : "))
    Z = U / I
    print("L'impédance est de", Z, "ohms.")
    
elif choix == "8":
    # Calcul de la réactance
    f = float(input("Entrez la fréquence en hertz : "))
    L = float(input("Entrez l'inductance en henrys : "))
    Xl = 2 * 3.14 * f * L
    print("La réactance est de", Xl, "ohms.")
    
elif choix == 9:
    print("\nCalcul de l'impédance complexe\n")
    print("Veuillez choisir l'une des formules suivantes :")
    print("1 - Z = R + jX")
    print("2 - Z = R - jX")
    print("3 - Z = |Z|∠θ")
    choix_formule = int(input("Entrez le numéro de la formule choisie : "))

    if choix_formule == 1:
        R = float(input("Entrez la valeur de la résistance (en Ω) : "))
        X = float(input("Entrez la valeur de la réactance (en Ω) : "))
        Z = complex(R, X)
        print("L'impédance complexe est Z =", Z, "Ω")

    elif choix_formule == 2:
        R = float(input("Entrez la valeur de la résistance (en Ω) : "))
        X = float(input("Entrez la valeur de la réactance (en Ω) : "))
        Z = complex(R, -X)
        print("L'impédance complexe est Z =", Z, "Ω")

    elif choix_formule == 3:
        module = float(input("Entrez la valeur du module de l'impédance (en Ω) : "))
        angle = float(input("Entrez la valeur de l'angle θ (en degrés) : "))
        Z = complex(module * math.cos(math.radians(angle)), module * math.sin(math.radians(angle)))
        print("L'impédance complexe est Z =", Z, "Ω")

    else:
        print("Choix invalide")

