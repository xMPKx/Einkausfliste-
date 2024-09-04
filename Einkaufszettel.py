

einkaufsliste = ["Milch", "Brot", "Eier", "Käse", "Äpfel"]

def element_hinzufuegen(einkaufsliste, element):

    if element not in einkaufsliste:
        einkaufsliste.append(element)

    else:
        print("bereits eingekauft")

    
    return einkaufsliste

result= element_hinzufuegen(einkaufsliste, "Kaffee")
print(result)


def element_entfernen(einkaufsliste, element):

    if element in einkaufsliste:
        einkaufsliste.remove(element)

    return einkaufsliste


result2= element_entfernen(einkaufsliste, "Brot")
print(result2)


def einkaufsliste_anzeigen(einkaufsliste):
    print("Aktuelle Einkaufsliste")

    for i, element in enumerate(einkaufsliste, start=1):
        print(f"{i}, {element}")

    


einkaufsliste_anzeigen(einkaufsliste)

def hauptprogramm():

    print("willkommen bei der Einkaufsliste")
    while True:
        print("\nWähle eine Aktion:")
        print("1. Element hinzufügen")
        print("2. Element entfernen")
        print("3. Einkaufsliste anzeigen")
        print("4. Beenden")
        
        auswahl = input("Bitte wähle eine Option (1-4): ")

        if auswahl == "1":
            element = input("Gib das Element ein, das du hinzufügen möchtest: ")
            element_hinzufuegen(einkaufsliste, element)
        elif auswahl == "2":
            element = input("Gib das Element ein, das du entfernen möchtest: ")
            element_entfernen(einkaufsliste, element)
        elif auswahl == "3":
            einkaufsliste_anzeigen(einkaufsliste)
        elif auswahl == "4":
            print("Programm beendet. Danke fürs Benutzen!")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle eine Option von 1 bis 4.")

hauptprogramm()


