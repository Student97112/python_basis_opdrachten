# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Stel de vragen aan de gebruiker
antwoord1 = input("Wat vind je van de huidige regering?\n")
antwoord2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
antwoord3 = input("Wat vind jij de mooiste stad van Nederland?\n")

# Open een tekstbestand om de antwoorden op te slaan (of maak het bestand als het niet bestaat)
with open("enquete_resultaten.txt", "a") as file:
    # Schrijf de antwoorden naar het tekstbestand
    file.write(f"Antwoord op vraag 1: {antwoord1}\n")
    file.write(f"Antwoord op vraag 2: {antwoord2}\n")
    file.write(f"Antwoord op vraag 3: {antwoord3}\n")

print("Bedankt voor het invullen van de enquête!")
