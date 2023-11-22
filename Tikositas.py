import tkinter as tk
from tkinter import messagebox

import string
import beleptetes
import Snake

chars = " " +string.digits + string.ascii_letters
chars = list(chars)
key = "gkZHXi7D28mBpU9e0Lt54McR3OWq6dEfKwFhsvNnAJPYrQuICjSx1yVbzLopTaGyjXq"+" "


#ENCRYPT
plain_text = beleptetes.jelszo_bekerese()
score=Snake.score
processed_chars = set() # egy halmazt a már feldolgozott karakterek tárolására
eredeti_chars=set() #egy halmazt a nem feldolgozott karakterek tárolására

def szam_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isdigit() and char not in processed_chars:
            index = chars.index(char)
            eredeti_chars.add(index)
            #print(f"szám:{index}")
            #if 0 <= index < len(key):  azt ellenőrzi, hogy az index változó egy érvényes tartományban van-e. Itt a kulcsban való helynek 0 és a kulcs hossza között kell lennie.
            cipher_text += key[index]
            processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            #else:
                #cipher_text += char
        else:
            cipher_text += char

    return cipher_text

def kisbetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.islower() and char not in processed_chars:
            index = chars.index(char)
            eredeti_chars.add(index)
            #print(f"kisbetu:{index}")
            #if 0 <= index < len(key):
            cipher_text += key[index]
            processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            #else:
                #cipher_text += char
        else:
            cipher_text += char

    return cipher_text

def nagybetu_titkositas(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isupper() and char not in processed_chars:
            index = chars.index(char)
            eredeti_chars.add(index)
            #print(f"nagybetu:{index}")
            #if 0 <= index < len(key):
            cipher_text += key[index]
            processed_chars.add(key[index])  # Jelöld meg, hogy ezt a karaktert már feldolgoztad
            #else:
                #cipher_text += char
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
        if index in eredeti_chars:
            plain_text += chars[index]
        else:
            plain_text += key[index]

    return plain_text

decrypted_text = visszafejtes(encrypted_text, key)
print(f"decrypted message: {decrypted_text}")

#print(processed_chars)
#print(eredeti_chars)

def bejelentkezes():
    felhasznalonev = felhasznalonev_entry.get()
    jelszo = jelszo_entry.get()

    with open("jelszo.txt", "r") as file:
        adatok = file.readlines()

    bejelentkezes_sikeres = False
    for sor in adatok:
        try:
            felhasznalonev_fajl, jelszo_titkos = sor.strip().split(";")
        except ValueError:
            messagebox.showerror("Hiba", "Hibás formátum a fájlban.")
            return

        if felhasznalonev == felhasznalonev_fajl and jelszo == decrypted_text:
            bejelentkezes_sikeres = True
            break

    if bejelentkezes_sikeres:
        messagebox.showinfo("Bejelentkezés", "Sikeres bejelentkezés!")
        reset_fields()
    else:
        messagebox.showerror("Hiba", "Hibás felhasználónév vagy jelszó!")

def reset_fields():
    felhasznalonev_entry.delete(0, tk.END)
    jelszo_entry.delete(0, tk.END)

# A Tkinter ablak létrehozása
root = tk.Tk()
root.title("Bejelentkezés")

# Méretek és helyköz beállítása
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.configure(padx=10, pady=10)

# Felhasználónév és jelszó beviteli mezők létrehozása
felhasznalonev_label = tk.Label(root, text="Felhasználónév:")
felhasznalonev_label.pack()

felhasznalonev_entry = tk.Entry(root)
felhasznalonev_entry.pack()

jelszo_label = tk.Label(root, text="Jelszó:")
jelszo_label.pack()

jelszo_entry = tk.Entry(root, show="*")  # A jelszó mező tartalmát csillagokkal jelenítjük meg
jelszo_entry.pack()

# Bejelentkezés gomb létrehozása
bejelentkezes_gomb = tk.Button(root, text="Bejelentkezés", command=bejelentkezes)
bejelentkezes_gomb.pack()

# Az ablak megjelenítése
root.mainloop()