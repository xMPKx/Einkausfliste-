einkaufsliste = {
    "Apfel": [2, 5],  # Preis pro Stück, benötigte Menge
    "Brot": [3, 2],
    "Milch": [1.5, 3],
    "Eier": [0.5, 12],
    "Käse": [5, 1]
}




def kauf(einkaufsliste, budget):

    kaufbare_artikel = {}

    nicht_erschwinglich = []

    gesamtkosten = 0

    for artikel, info in einkaufsliste.items():
        kosten = info[0] * info[1]

        if kosten <= budget:
            kaufbare_artikel[artikel] = kosten
            gesamtkosten += kosten
            budget -= kosten

        else:
            nicht_erschwinglich.append(artikel)


    return kaufbare_artikel, nicht_erschwinglich, gesamtkosten, budget


budget = 20

kaufbare_artikel, gesamtkosten, restbudget, nicht_erschwinglich = kauf(einkaufsliste, budget)

print(kaufbare_artikel)
print(gesamtkosten)
print(restbudget)
print(nicht_erschwinglich)




