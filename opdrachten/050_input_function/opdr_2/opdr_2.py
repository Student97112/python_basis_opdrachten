# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een initiële lijst met de gasten
gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Print de initiële lijst op het scherm
print(gasten)

# Verwijder Marie uit de lijst
gasten.remove("Marie")

# Print de aangepaste lijst op het scherm
print(gasten)

# Voeg George naast Kees toe aan de lijst
kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")

# Print de uiteindelijke lijst op het scherm
print(gasten)
