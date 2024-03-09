# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

# Maak een lege lijst om getallen van 1 t/m 10 in op te slaan
getallen = []

# Vul de lijst met getallen van 1 t/m 10 met behulp van een loop
for i in range(1, 11):
    # Controleer of het getal groter is dan 4
    if i > 4:
        # Voeg het getal toe aan de lijst
        getallen.append(i)

# Print de getallen die groter zijn dan 4 op het scherm
print(getallen)
