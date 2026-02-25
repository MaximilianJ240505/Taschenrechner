ergebnisse = []
weiterverwenden = "nein"
while True:
    while True:
        try:
            if weiterverwenden == "ja":
                number_1 = ergebnis
            else :
                number_1 = int(input("Erste Zahl: "))
            break
        except:
            print("Das ist keine Zahl! Versuch es nochmal.")
    while True:
        rechenart = input("Wie willst du rechnen? (+, -, *, /) ")
        if rechenart == "+" or rechenart == "-" or rechenart == "*" or rechenart == "/" or rechenart == "%":
            break
        else:
            print("Ungültige Rechenart! Bitte erneut versuchen.")
    while True:
        try:
            number_2 = int(input("Zweite Zahl: "))
            break
        except:
            print("Das ist keine Zahl! Versuch es nochmal.")
    if rechenart == "/" and number_2 == 0:
        print("Du kannst nicht durch 0 teilen!")
    elif rechenart == "+":
        ergebnis = number_1 + number_2
    elif rechenart == "-":
        ergebnis = number_1 - number_2
    elif rechenart == "*":
        ergebnis = number_1 * number_2
    elif rechenart == "/":
        ergebnis = number_1 / number_2
    elif rechenart == "%":
        ergebnis = number_1 * number_2 / 100
    if rechenart != "/" or number_2 != 0:
        ergebnisse.append(ergebnis)
        print(f"Das Ergebnis ist: {ergebnis}")
        print("---------------------------------------")
    antwort = input("Willst du noch weiter rechnen? Ja / Nein: ").lower()
    if antwort == "nein":
        break
    
    if antwort == "ja":
        weiterverwenden = input(f"Ergebnis weiterverwenden? Ja / Nein").lower()
for nummer, ergebnis in enumerate(ergebnisse, 1):
    print(f"{nummer}. {ergebnis}")
