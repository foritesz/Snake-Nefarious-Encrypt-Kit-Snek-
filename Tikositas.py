import random
import string
import beleptetes
import Snake

chars = " " +string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = beleptetes.jelszo_bekerese()
score=4
processed_chars = set() # egy halmazt a már feldolgozott karakterek tárolására
eredeti_chars=set()

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
            index = chars.index(char)
            eredeti_chars.add(index)
            #original_char = plain_text[index]
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
            index = chars.index(char) #ord() függvény az adott karakter Unicode kódját adja vissza úgy hogy a kis abetütől kezdi ek nézni
            eredeti_chars.add(index)
            #original_char = plain_text[index]
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
            index = chars.index(char)
            eredeti_chars.add(index)
            #original_char = plain_text[index]
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

"""def unicode(plain_text):
    keykod=""
    for letter in plain_text:
        index = chars.index(letter)
        text=plain_text[index]
        index2=str(index)
        keykod +=index2+','+text

    return keykod"""

#key2=unicode(plain_text)
encrypted_text = tikositas_pontszerint(score, plain_text)
felh=beleptetes.felhasznalonev()

def fajl():
    with open('jelszo.txt', 'r') as f:
        lines = f.readlines()

    with (open('jelszo.txt', 'w') as f):
        for line in lines:
            parts = line.strip().split(';')
            if len(parts) == 2 and felh in parts[0]:
                parts[1] = encrypted_text+'\n'
                line = ';'.join(parts)
            f.write(line)



print(f"original message : {plain_text}")
print(f"encrypted message: {encrypted_text}")

fajl()
def visszafejtes(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    return plain_text

decrypted_text = visszafejtes(encrypted_text, key)
print(f"decrypted message: {decrypted_text}")

print(processed_chars)
print(eredeti_chars)