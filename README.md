# Einkausfliste


Dieses Projekt ist ein einfaches Python-Programm zur Verwaltung einer Einkaufsliste. Es ermöglicht dem Benutzer, Elemente zur Einkaufsliste hinzuzufügen, zu entfernen, die aktuelle Einkaufsliste anzuzeigen und das Programm zu beenden. Die Benutzerinteraktion erfolgt über eine einfache Textschnittstelle.

 Funktionen

Das Programm enthält die folgenden Funktionen:

1. **`element_hinzufuegen(einkaufsliste, element)`**: 
   - Diese Funktion fügt ein neues Element zur Einkaufsliste hinzu, wenn es noch nicht vorhanden ist.
   - Gibt eine Nachricht aus, wenn das Element bereits in der Liste ist.

2. **`element_entfernen(einkaufsliste, element)`**: 
   - Diese Funktion entfernt ein Element aus der Einkaufsliste, wenn es vorhanden ist.
   - Gibt die aktualisierte Einkaufsliste zurück.

3. **`einkaufsliste_anzeigen(einkaufsliste)`**: 
   - Diese Funktion zeigt die aktuelle Einkaufsliste in einer nummerierten Reihenfolge an.
   - Zeigt eine Nachricht an, wenn die Einkaufsliste leer ist.

4. **`hauptprogramm()`**: 
   - Das Hauptprogramm bietet eine Benutzerschnittstelle, um die Einkaufsliste zu verwalten.
   - Der Benutzer kann die folgenden Aktionen auswählen:
     - Element hinzufügen
     - Element entfernen
     - Einkaufsliste anzeigen
     - Programm beenden


zum zweiten Code "mit_budget"

Dieses Python-Programm hilft dabei, eine Einkaufsliste basierend auf einem bestimmten Budget zu erstellen. Es berechnet die Gesamtkosten für Artikel, die innerhalb des Budgets gekauft werden können, und listet die Artikel auf, die nicht erschwinglich sind.

Funktionen:
Einkaufsliste: Eine vordefinierte Einkaufsliste mit Artikelpreisen und benötigten Mengen.
Budgetverwaltung: Die Funktion kauf(einkaufsliste, budget) berechnet die Gesamtkosten der kaufbaren Artikel und aktualisiert das verbleibende Budget.
Ergebnisse: Die Funktion gibt eine Liste der kaufbaren Artikel, die Gesamtkosten, das verbleibende Budget und die nicht erschwinglichen Artikel zurück.
