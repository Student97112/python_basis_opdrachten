# Opdracht 1 lists
# Naam student:
# Groep:

# Maak een list aan om dictionaries op te slaan
personen = []

# Maak 4 dictionaries om gegevens van personen in op te slaan
persoon1 = { "id": 1, "voornaam": "Jan", "achternaam": "Jansen" }
persoon2 = { "id": 2, "voornaam": "Piet", "achternaam": "Pietersen" }
persoon3 = { "id": 3, "voornaam": "Kees", "achternaam": "Klaassen" }
persoon4 = { "id": 4, "voornaam": "Marie", "achternaam": "Janssen" }

# Voeg de 4 dictionaries toe aan de list
personen.extend([persoon1, persoon2, persoon3, persoon4])

# Print de volledige naam van de 2e persoon op het scherm
print(personen[1]["voornaam"], personen[1]["achternaam"])

