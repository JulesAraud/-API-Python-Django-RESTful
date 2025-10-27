temp = input("Saisissez la température que vous souhaitez convertir: ")

degre = int(temp[:-1])
unite = temp[-1].upper()

if unite == "C":

    result = (degre * 9/5) + 32
    print(f"La température en Fahrenheit est de {result:.1f} degrés.")
elif unite == "F":

    result = (degre - 32) * 5/9
    print(f"La température en Celsius est de {result:.1f} degrés.")
else:
    print("Unité invalide. Veuillez terminer par 'C' ou 'F'.")
