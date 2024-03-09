# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...

# Definieer de functie voor y in termen van x
def bereken_y(x):
    return 4 * x**3 - 2 * x**2 - 1

# Testgevallen
x_waarden = [1, 2, 0]

# Berekeningen en uitvoer voor elk testgeval
for x in x_waarden:
    y = bereken_y(x)
    print(f"Bij x = {x}, is y = {y}")

