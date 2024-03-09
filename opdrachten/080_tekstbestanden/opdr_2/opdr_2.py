# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....

import random

# Genereer een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)

# Initialisatie van het aantal pogingen
aantal_pogingen = 0

print("Raad mijn geheime getal")

# Blijf vragen om een gok totdat de gebruiker het juiste getal heeft geraden
while True:
    gok = int(input())
    aantal_pogingen += 1
    
    if gok < geheim_getal:
        print("hoger")
    elif gok > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        break


