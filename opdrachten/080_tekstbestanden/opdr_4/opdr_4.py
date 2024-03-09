# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

# Vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Open een tekstbestand om de antwoorden op te slaan (of maak het bestand als het niet bestaat)
with open("feestgangers.txt", "a") as file:
    # Loop door de vragen en vraag antwoorden aan de gebruiker
    antwoorden = {}
    for vraag in vragen:
        antwoord = input(vraag + "\n")
        antwoorden[vraag] = antwoord
    
    # Schrijf de antwoorden naar het tekstbestand
    file.write("----\n")
    for vraag, antwoord in antwoorden.items():
        file.write(f"{vraag.lower()}: {antwoord}\n")
    file.write("----\n")

print("Bedankt voor het invullen!")
print("See you at the party.")
