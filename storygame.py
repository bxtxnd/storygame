import tkinter as tk
from tkinter import messagebox
import random

# Karakter osztály
class Karakter:
    def __init__(self, nev, hangszorok):
        self.nev = nev
        self.hangszorok = hangszorok
    
    def beszél(self):
        return f"{self.nev}: {random.choice(self.hangszorok)}"
    
    def parbeszed(self, jatekos_valasz):
        if self.nev == "Anna":
            if jatekos_valasz == 1:
                return f"{self.nev}: Mi történik itt? Ez a hely még nem létezik térképeken... Én csak egyet tudok, együtt kell maradnunk!"
            elif jatekos_valasz == 2:
                return f"{self.nev}: Készen állok, de nem tudom, hogy mi vár ránk... vigyázz, nem mindenkiben lehet megbízni."
            elif jatekos_valasz == 3:
                return f"{self.nev}: Miért éppen most? Mi lehet itt, ami figyel minket?"
        
        elif self.nev == "László":
            if jatekos_valasz == 1:
                return f"{self.nev}: Igazad van. Ez mind olyan zűrös... Biztos, hogy helyes döntés lesz segíteni, de figyelj, valami követ minket!"
            elif jatekos_valasz == 2:
                return f"{self.nev}: Készen állok, de mibe keveredtünk? Az erdő veszélyesebb, mint bármi, amit el tudtam képzelni."
            elif jatekos_valasz == 3:
                return f"{self.nev}: Valami nem stimmel... de ha el akarjuk hagyni ezt a helyet, gyorsnak kell lennünk!"
        
        elif self.nev == "Zoltán":
            if jatekos_valasz == 1:
                return f"{self.nev}: Mi folyik itt?", "Miért hozott ide minket a sors? Eddig semmi hasonlót nem láttam."
            elif jatekos_valasz == 2:
                return f"{self.nev}: Figyelj, ha fel akarunk jutni a hegyre, nem szabad megállnunk! A hegycsúcs, a kulcs."
            elif jatekos_valasz == 3:
                return f"{self.nev}: Minél tovább itt vagyunk, annál inkább érzem, hogy valami figyel minket. Jobb lesz elindulnunk."

        elif self.nev == "Dóra":
            if jatekos_valasz == 1:
                return f"{self.nev}: Ne aggódj, a titokzatos erdő ismerős számomra. Van egy barlang, ami elrejt minket."
            elif jatekos_valasz == 2:
                return f"{self.nev}: Miért keresnél biztonságot a kastélyban? Még sokan elestek ott."
            elif jatekos_valasz == 3:
                return f"{self.nev}: Ha túl akarjuk élni, gyorsan cselekednünk kell. A kastély a legjobb esélyünk."
        
        elif self.nev == "Gábor":
            if jatekos_valasz == 1:
                return f"{self.nev}: Meg kell határoznunk, miért vagyunk itt. Lehet, hogy mindez egy próbát jelent."
            elif jatekos_valasz == 2:
                return f"{self.nev}: Mindent kockáztatnunk kell. Nézd meg a titkos bejáratot! Ott mindent megtudhatunk."
            elif jatekos_valasz == 3:
                return f"{self.nev}: Nem jó itt maradni... de a választás a tiéd. Ki kell jutnunk, és kockáztatni!"

# Szenárió osztály
class Szenario:
    def __init__(self, cim, leiras, karakterek):
        self.cim = cim
        self.leiras = leiras
        self.karakterek = karakterek
    
    def belep(self):
        dialog = f"\nBelépsz a következő helyszínre: {self.cim}\n{self.leiras}\n\n"
        for karakter in self.karakterek:
            dialog += karakter.beszél() + "\n"
        
        return dialog

# Játék GUI osztály
class Jatek:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaland Játék")
        
        # Karakterek
        self.karakter_1 = Karakter("Anna", ["Helló, hogy vagy?", "Készen állok bármire!", "Mi történik itt?"])
        self.karakter_2 = Karakter("László", ["Gyerünk, csináljuk!", "Ezt nem érzem jól...", "Veled vagyok."])
        self.karakter_3 = Karakter("Zoltán", ["Mi folyik itt?", "Jó lenne egy kis pihenő...", "Mit csináljunk most?"])
        self.karakter_4 = Karakter("Dóra", ["Nincs visszaút!", "Azt hiszem, most már túl késő!", "Ne aggódj, segítek."])
        self.karakter_5 = Karakter("Gábor", ["Készen állok a harcra!", "Mi a terv?", "Tartsd magad közel hozzám."])
        
        # Szenáriók
        self.szenario_1 = Szenario("Misztikus Erdő", "Sűrű köd lepi el az erdőt, a fák hatalmasak és sötétek. Furcsa zajok hallatszanak a távolból. Valami nem stimmel, valami figyel téged...", [self.karakter_1, self.karakter_2])
        self.szenario_2 = Szenario("Elhagyatott Kastély", "Egy elhagyatott kastély emelkedik a domb tetején. A szél süvít, és furcsa suttogásokat hallasz az épületből. Valami szörnyű titok rejlik itt.", [self.karakter_1, self.karakter_3])
        self.szenario_3 = Szenario("Mesés Tengerpart", "A homok forró a lábad alatt, miközben a tenger morajlását hallgatod a távolban. Az óceán titkai örökre rejtve maradnak?", [self.karakter_2])
        self.szenario_4 = Szenario("Ódon Temető", "Az éjszaka sötétjében egy régi temetőben vagy. A köd leereszkedik, és szélfúvás hallatszik. Valami épp most ébredt fel.", [self.karakter_3])
        self.szenario_5 = Szenario("Titkos Barlang", "A sötét barlangban a levegő nehéz, és a csöpögő víz zajától egy hátborzongató csend telepedik a helyre. Mi lehet itt elrejtve?", [self.karakter_4, self.karakter_5])
        self.szenario_6 = Szenario("Fagyos Hegycsúcs", "A hegycsúcsot fagy borítja, a szél szinte átszúrja a ruházatodat. A hóviharral küzdesz, miközben feljutsz a csúcsra. Miért jöttél ide?", [self.karakter_4, self.karakter_5])
        
        # Szövegdoboz
        self.text_output = tk.Text(self.root, height=15, width=60)
        self.text_output.pack()
        
        # Válasz gombok
        self.button1 = tk.Button(self.root, text="Mi történik itt?", command=lambda: self.valasz(1))
        self.button1.pack()
        
        self.button2 = tk.Button(self.root, text="Készen állok bármire!", command=lambda: self.valasz(2))
        self.button2.pack()
        
        self.button3 = tk.Button(self.root, text="Valami nincs rendben...", command=lambda: self.valasz(3))
        self.button3.pack()
        
        # Szenáriók választása
        self.szenariumok = [self.szenario_1, self.szenario_2, self.szenario_3, self.szenario_4, self.szenario_5, self.szenario_6]
        
        # Játék kezdése
        self.start_game()

    def start_game(self):
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, "Elérhető helyszínek:\n")
        for idx, szenario in enumerate(self.szenariumok, 1):
            self.text_output.insert(tk.END, f"{idx}. {szenario.cim}\n")
        
        self.text_output.insert(tk.END, "\nVálassz egy helyszínt (1-6): ")
        self.root.after(1000, self.szenarium_kivalasztas)

    def szenarium_kivalasztas(self):
        valasz = int(input("Válassz egy helyszínt (1-6): "))
        if valasz < 1 or valasz > 6:
            messagebox.showerror("Hiba", "Érvénytelen választás!")
            return
        szenario = self.szenariumok[valasz-1]
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, szenario.belep())
        
    def valasz(self, jatekos_valasz):
        self.text_output.insert(tk.END, f"Válaszoltál: {jatekos_valasz}\n")
        for karakter in self.szenariumok[0].karakterek:
            self.text_output.insert(tk.END, karakter.parbeszed(jatekos_valasz) + "\n")
        
# Indítás
if __name__ == "__main__":
    window = tk.Tk()
    game = Jatek(window)
    window.mainloop()
