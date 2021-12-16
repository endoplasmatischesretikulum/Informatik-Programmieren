# Der Benutzer gibt eine Schweizer Note ein.
# Das Programm berechnet die Note ins Amerikanische Schulsystem.

note = float(input("Note eingeben:"))

# Wenn die Note zwischen 5.5 und 6 ist, ist die Amerikanische Note "A".

if note >= 5.5 and note <= 6:
    print("A")
    
# Wenn die Note zwischen 4.5 und 5.4 ist, ist die Amerikanische Note "B".

elif note >= 4.5 and note <= 5.4:
    print("B")
    
# Wenn die Note zwischen 4.0 und 4.4 ist, ist die Amerikanische Note "c".

elif note >= 4.0 and note <= 4.4:
    print("C")
    
# Wenn die Note unter 4.0 ist, ist die Amerikanische Note "F".

elif note < 4.0:
    print("F")
    
# Wenn der Benutzer einen Fehler bei der Eingabe macht, gibt der Computer "Ungültige Eingabe" aus.

else:
    print("Ungültige Eingabe!")
