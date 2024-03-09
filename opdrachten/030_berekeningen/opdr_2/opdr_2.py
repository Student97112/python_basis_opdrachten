# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

c = ...
f = ...

print()

# Functie om Celsius naar Fahrenheit om te rekenen
def celsius_naar_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Functie om Fahrenheit naar Celsius om te rekenen
def fahrenheit_naar_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Testgevallen
c = -12
f = 144

# Berekeningen en uitvoer voor het eerste testgeval
fahrenheit_resultaat = celsius_naar_fahrenheit(c)
print(f"{c} graden Celsius is gelijk aan {fahrenheit_resultaat} graden Fahrenheit")

celsius_resultaat = fahrenheit_naar_celsius(f)
print(f"{f} graden Fahrenheit is gelijk aan {celsius_resultaat} graden Celsius")

# Testgeval 2
c = 62.2
f = 96

# Berekeningen en uitvoer voor het tweede testgeval
fahrenheit_resultaat = celsius_naar_fahrenheit(c)
print(f"{c} graden Celsius is gelijk aan {fahrenheit_resultaat} graden Fahrenheit")

celsius_resultaat = fahrenheit_naar_celsius(f)
print(f"{f} graden Fahrenheit is gelijk aan {celsius_resultaat} graden Celsius")
