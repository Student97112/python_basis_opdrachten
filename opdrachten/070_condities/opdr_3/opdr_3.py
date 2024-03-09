# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

# Gegeven variabelen
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Vraag de leeftijd van de bezoeker
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de leeftijdsgroep van de bezoeker
for groep, leeftijdsgrenzen in leeftijd.items():
    if leeftijdsgrenzen[0] <= leeftijd_input <= leeftijdsgrenzen[1]:
        leeftijdsgroep = groep
        break

# Bereken de korting en de toegangsprijs op basis van de leeftijdsgroep
korting_percentage = kortings_percentages[leeftijdsgroep]
korting_bedrag = normale_toegangsprijs * (korting_percentage / 100)
toegangsprijs = normale_toegangsprijs - korting_bedrag

# Print de output
print(f"U behoort tot de groep {leeftijdsgroep}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {toegangsprijs}")
