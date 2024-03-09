# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Maak de initiële lijst met pizza's
pizza_s = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabetische volgorde
pizza_s.sort()

# Voeg een nieuwe pizza toe naar eigen smaak
pizza_s.append('yo-favorito')

# Verwijder de pizza die je het minst lekker vindt
pizza_s.remove('olivio')

# Print de eerste 3 pizza's uit de lijst
print(pizza_s[:3])

# Print alleen de middelste pizza uit de lijst
print(pizza_s[len(pizza_s)//2])

# Print de laatste 3 pizza's uit de lijst
print(pizza_s[-3:])
