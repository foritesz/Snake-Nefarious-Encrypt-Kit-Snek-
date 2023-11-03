import random
import string

chars = " " + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""
index_file = open("jelszo.txt", "w")  # Fájl megnyitása írásra

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    index_file.write(f"{index} ")  # Az indexet írjuk a fájlba

index_file.close()  # Fájl bezárása

print(f"original message : {plain_text}")
print(f"encrypted message: {cipher_text}")

# DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""
index_file = open("jelszo.txt", "r")  # Fájl megnyitása olvasásra
indices = index_file.read().split()  # Beolvasott indexek szétválasztása

for index in indices:
    index = int(index)
    plain_text += chars[index]

index_file.close()  # Fájl bezárása

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")
