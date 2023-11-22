import tkinter as tk
from tkinter import messagebox
from Tikositas import decrypted_text


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
