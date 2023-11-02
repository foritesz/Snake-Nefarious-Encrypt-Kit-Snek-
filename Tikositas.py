import random
import string
import beleptetes
import Snake

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = beleptetes.jelszo_bekerese()
score=Snake.score
key = "your_encryption_key_here"  # Az itt lévő "your_encryption_key_here" helyére írd be a saját titkosítási kulcsodat

def szam_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isdigit():
            index = int(char)
            if 0 <= index < len(key):
                cipher_text += key[index]
            else:
                cipher_text += char
        else:
            cipher_text += char
    return cipher_text

def kisbetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.islower():
            index = ord(char) - ord('a')
            if 0 <= index < len(key):
                cipher_text += key[index]
            else:
                cipher_text += char
        else:
            cipher_text += char
    return cipher_text

def nagybetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isupper():
            index = ord(char) - ord('A')
            if 0 <= index < len(key):
                cipher_text += key[index]
            else:
                cipher_text += char
        else:
            cipher_text += char
    return cipher_text

def tikositas_pontszerint(score, plain_text):
    if score >= 2:
        plain_text = szam_titkositas(plain_text)
    if score >= 3:
        plain_text = kisbetu_titkositas(plain_text)
    if score == 4:
        plain_text = nagybetu_titkositas(plain_text)

    return plain_text

encrypted_text = tikositas_pontszerint(score, plain_text)
felh=beleptetes.felhasznalonev()
def fajl():
    with open('jelszo.txt', 'r') as f:
        lines = f.readlines()

    with open('jelszo.txt', 'w') as f:
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) == 2 and felh in parts[0]:
                parts[1] = encrypted_text+'\n'
                line = ';'.join(parts)
            f.write(line)




print(f"original message : {plain_text}")
print(f"encrypted message: {encrypted_text}")

fajl()

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")