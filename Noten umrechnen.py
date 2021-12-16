note = float(input("Note eingeben:"))

if note >= 5.5 and note <= 6:
    print("A")
elif note >= 4.5 and note <= 5.4:
    print("B")
elif note >= 4.0 and note <= 4.4:
    print("C")
elif note < 4.0:
    print("F")
else:
    print("Ungültige Eingabe!")