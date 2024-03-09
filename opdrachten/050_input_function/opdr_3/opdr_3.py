# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om een lijst met objecten in te vullen en splits de input op komma's
input_string = input("Voer minimaal 5 objecten gescheiden door komma's in: ")
objecten = input_string.split(',')

# Strip eventuele spaties aan het begin en einde van elk object
objecten = [object.strip() for object in objecten]

# Sorteer de lijst in omgekeerde volgorde
objecten.sort(reverse=True)

# Print de gesorteerde lijst op het scherm
print(objecten)

