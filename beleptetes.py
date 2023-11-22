# Beléptető rendszer



def regisztracio():
    sikeres = True
    felhasznalo_email=felhasznalonev()
    felhasznalo_jelszava=jelszo_bekerese()
    i=1
    while not jelszo_ellenorzes(felhasznalo_jelszava,"Kérem ismételje meg a jelszót: "):
        print("Nem egyezik a két jelszó!")
        i+=1
        if i>3:
            sikeres=False
            break
    if sikeres:
        with open("jelszo.txt", "a",encoding="utf-8") as fajl:
            fajl.write("\n"+felhasznalo_email + ";" + felhasznalo_jelszava)
    return sikeres

def felhasznalonev():
    felhasznalo_email=input("Kérek egy felhasználói nevet (email): ")
    while " " in felhasznalo_email:
        felhasznalo_email = input("Nem megfelelő az email!\nKérek egy felhasználói nevet: ")
    return felhasznalo_email

def jelszo_bekerese():
    felhasznalo_jelszava=input("Kérek egy jelszót (1,a,A,min 8 és max 12 karakteres): ")
    rossz_jelszo=True
    while rossz_jelszo:
        rossz_jelszo=False
        if len(felhasznalo_jelszava) <8 and len(felhasznalo_jelszava)>12:
            rossz_jelszo=True
        van_e_benne=0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isnumeric():
                van_e_benne+=1
        if van_e_benne==0:
            rossz_jelszo=True

        van_e_benne = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].isupper():
                van_e_benne += 1
        if van_e_benne == 0:
                rossz_jelszo = True

        van_e_benne = 0
        for i in range(len(felhasznalo_jelszava)):
            if felhasznalo_jelszava[i].islower():
                van_e_benne += 1
        if van_e_benne == 0:
            rossz_jelszo = True

        if rossz_jelszo==True:
            felhasznalo_jelszava = input("Nem megfelelő a jelszó!/nKérek egy jelszót (1,a,A,min 8 és max 12 karakteres): ")
        else:
            rossz_jelszo=False

    return felhasznalo_jelszava

def jelszo_ellenorzes(felhasznalo_jelszava, uzenet):
    jelszo2=input(uzenet)
    if jelszo2==felhasznalo_jelszava:
        ok_jelszo=True
    else:
        ok_jelszo=False
    return  ok_jelszo

def felhasznalo_ellenorzese(felhasznalo):
    jelszo=""
    with open ("jelszo.txt","r",encoding="utf-8") as fajl:
        for sor in fajl:
            lista=sor.strip()
            user = lista.split(";")
            if user[0]==felhasznalo:
                jelszo=user[1]
    return jelszo

def beleptetes():
    ok_regisztracio=True
    jelszo=felhasznalo_ellenorzese(felhasznalonev())
    if jelszo=="":
        print("Nincs ilyen felhasználó, kérem regissztráljon!")
        ok_regisztracio=False
    i=1
    while jelszo !="":
        if jelszo_ellenorzes(jelszo,"Kérem a jelszót: "):
            break
        i+=1
        if i>3:
            print("Nem sikerült kitalálni a jelszót!")
            ok_regisztracio=False
            break
    return ok_regisztracio
def jelszo_hossz():

    jelszohossz=jelszo_bekerese()
    return len(jelszohossz)



#Innen indul a program
if __name__=="__main__":


    if regisztracio():
       if beleptetes():
           print("Üdv a fedélzeten!")
       else:
           print("Nem sikerült belépnie!")
    else:
        print("A regisztráció miatt, nem történt beléptetés")

    import Snake
    import Tikositas