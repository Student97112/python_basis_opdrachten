# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

# Beschikbare toppings
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst met alleen de namen van de toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze uit de beschikbare toppings
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze van de gebruiker in de lijst met beschikbare toppings zit
gekozen_topping = None
for topping in toppings:
    if keuze.lower() == topping[0]:
        gekozen_topping = topping
        break

# Als de gekozen topping bestaat, print de naam en de prijs, anders print een foutmelding
if gekozen_topping:
    print(f"U heeft {gekozen_topping[0]} besteld. Dat kost {gekozen_topping[1]}")
else:
    print("Uw keuze zit niet in ons assortiment")
