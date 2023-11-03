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
score=4
key = "your_encryption_key_here"  # Az itt lévő "your_encryption_key_here" helyére írd be a saját titkosítási kulcsodat
processed_chars = set() # egy halmazt a már feldolgozott karakterek tárolására
"""def atlakitas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                cipher_text += "%" + char
            else:
                cipher_text += "!" + char
        elif char.isdigit():
            cipher_text += "=" + char
        else:
            cipher_text += char

    return cipher_text"""

def szam_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isdigit() and char not in processed_chars:
            index = int(char)
            print(f"szám:{index}")
            if 0 <= index < len(key):
                cipher_text += key[index]
                processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            else:
                cipher_text += char
        else:
            cipher_text += char

    return cipher_text

def kisbetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.islower() and char not in processed_chars:
            index = ord(char) - ord('a')
            print(f"kisbetu:{index}")
            if 0 <= index < len(key):
                cipher_text += key[index]
                processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            else:
                cipher_text += char
        else:
            cipher_text += char

    return cipher_text

def nagybetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isupper() and char not in processed_chars:
            index = ord(char) - ord('A')
            print(f"nagybetu:{index}")
            if 0 <= index < len(key):
                cipher_text += key[index]
                processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            else:
                cipher_text += char
        else:
            cipher_text += char

    return cipher_text

def tikositas_pontszerint(score, plain_text):
    """if score >= 1:
        plain_text = atlakitas(plain_text)"""
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

