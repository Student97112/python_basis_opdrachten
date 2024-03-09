# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # Controleer of het een letter is
            offset = 5
            if char.islower():  # Controleer of het een kleine letter is
                encrypted_char = chr(((ord(char) - 97 + offset) % 26) + 97)
            else:  # Het is een hoofdletter
                encrypted_char = chr(((ord(char) - 65 + offset) % 26) + 65)
        else:  # Het is geen letter, behoud de originele karakter
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

# Invoer van de gebruiker
text = input("Geef de tekst die je wilt encrypten: ")

# Versleutel de tekst
encrypted_text = encrypt(text)
print("Versleutelde tekst:")
print(encrypted_text)

