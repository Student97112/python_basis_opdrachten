# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(filename, text):
    """Schrijf tekst naar een bestand."""
    with open(filename, "a") as file:
        file.write(text + "\n")

# Voorbeeldgebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
