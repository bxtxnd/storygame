import random

class Karakter:
    def __init__(self, nev, hangszorok):
        self.nev = nev
        self.hangszorok = hangszorok
    
    def beszél(self):
        print(f"{self.nev}: {random.choice(self.hangszorok)}")
    
    def parbeszed(self, jatekos_valasz):
        # Anna válaszai
        if self.nev == "Anna":
            if jatekos_valasz == 1:
                print(f"{self.nev}: Mi történik itt? Ez a hely még nem létezik térképeken... Én csak egyet tudok, együtt kell maradnunk!")
            elif jatekos_valasz == 2:
                print(f"{self.nev}: Készen állok, de nem tudom, hogy mi vár ránk... vigyázz, nem mindenkiben lehet megbízni.")
            elif jatekos_valasz == 3:
                print(f"{self.nev}: Miért éppen most? Mi lehet itt, ami figyel minket?")
        
        # László válaszai
        elif self.nev == "László":
            if jatekos_valasz == 1:
                print(f"{self.nev}: Igazad van. Ez mind olyan zűrös... Biztos, hogy helyes döntés lesz segíteni, de figyelj, valami követ minket!")
            elif jatekos_valasz == 2:
                print(f"{self.nev}: Készen állok, de mibe keveredtünk? Az erdő veszélyesebb, mint bármi, amit el tudtam képzelni.")
            elif jatekos_valasz == 3:
                print(f"{self.nev}: Valami nem stimmel... de ha el akarjuk hagyni ezt a helyet, gyorsnak kell lennünk!")
        
        # Zoltán válaszai
        elif self.nev == "Zoltán":
            if jatekos_valasz == 1:
                print(f"{self.nev}: Mi folyik itt?", "Miért hozott ide minket a sors? Eddig semmi hasonlót nem láttam.")
            elif jatekos_valasz == 2:
                print(f"{self.nev}: Figyelj, ha fel akarunk jutni a hegyre, nem szabad megállnunk! A hegycsúcs, a kulcs.")
            elif jatekos_valasz == 3:
                print(f"{self.nev}: Minél tovább itt vagyunk, annál inkább érzem, hogy valami figyel minket. Jobb lesz elindulnunk.")

        # Dóra válaszai
        elif self.nev == "Dóra":
            if jatekos_valasz == 1:
                print(f"{self.nev}: Ne aggódj, a titokzatos erdő ismerős számomra. Van egy barlang, ami elrejt minket.")
            elif jatekos_valasz == 2:
                print(f"{self.nev}: Miért keresnél biztonságot a kastélyban? Még sokan elestek ott.")
            elif jatekos_valasz == 3:
                print(f"{self.nev}: Ha túl akarjuk élni, gyorsan cselekednünk kell. A kastély a legjobb esélyünk.")
        
        # Gábor válaszai
        elif self.nev == "Gábor":
            if jatekos_valasz == 1:
                print(f"{self.nev}: Meg kell határoznunk, miért vagyunk itt. Lehet, hogy mindez egy próbát jelent.")
            elif jatekos_valasz == 2:
                print(f"{self.nev}: Mindent kockáztatnunk kell. Nézd meg a titkos bejáratot! Ott mindent megtudhatunk.")
            elif jatekos_valasz == 3:
                print(f"{self.nev}: Nem jó itt maradni... de a választás a tiéd. Ki kell jutnunk, és kockáztatni!")

class Szenario:
    def __init__(self, cim, leiras, karakterek):
        self.cim = cim
        self.leiras = leiras
        self.karakterek = karakterek
    
    def belep(self):
        print(f"\nBelépsz a következő helyszínre: {self.cim}")
        print(self.leiras)
        
        # A karakterek beszélnek
        for karakter in self.karakterek:
            karakter.beszél()
        
        # Kérdések a játékosnak
        print("\nVálaszolj a kérdésre a megfelelő szám begépelésével.")
        print("1: Mi történik itt?")
        print("2: Készen állok bármire!")
        print("3: Valami nincs rendben...")
        
        jatekos_valasz = int(input("\nVálaszd ki a választott lehetőséget (1, 2, vagy 3): "))
        
        # A karakterek reagálnak a válaszra
        for karakter in self.karakterek:
            karakter.parbeszed(jatekos_valasz)

        return jatekos_valasz  # Visszaadja a válaszát, hogy a következő lépést végrehajthassuk

# Karakterek létrehozása
karakter_1 = Karakter(
    "Anna", 
    ["Helló, hogy vagy?", "Készen állok bármire!", "Mi történik itt?"]
)

karakter_2 = Karakter(
    "László", 
    ["Gyerünk, csináljuk!", "Ezt nem érzem jól...", "Veled vagyok."]
)

karakter_3 = Karakter(
    "Zoltán", 
    ["Mi folyik itt?", "Jó lenne egy kis pihenő...", "Mit csináljunk most?"]
)

karakter_4 = Karakter(
    "Dóra", 
    ["Nincs visszaút!", "Azt hiszem, most már túl késő!", "Ne aggódj, segítek."]
)

karakter_5 = Karakter(
    "Gábor", 
    ["Készen állok a harcra!", "Mi a terv?", "Tartsd magad közel hozzám."]
)

# Szenáriók létrehozása
szenario_1 = Szenario(
    "Misztikus Erdő",
    "Sűrű köd lepi el az erdőt, a fák hatalmasak és sötétek. Furcsa zajok hallatszanak a távolból. Valami nem stimmel, valami figyel téged...",
    [karakter_1, karakter_2]
)

szenario_2 = Szenario(
    "Elhagyatott Kastély",
    "Egy elhagyatott kastély emelkedik a domb tetején. A szél süvít, és furcsa suttogásokat hallasz az épületből. Valami szörnyű titok rejlik itt.",
    [karakter_1, karakter_3]
)

szenario_3 = Szenario(
    "Mesés Tengerpart",
    "A homok forró a lábad alatt, miközben a tenger morajlását hallgatod a távolban. Az óceán titkai örökre rejtve maradnak?",
    [karakter_2]
)

szenario_4 = Szenario(
    "Ódon Temető",
    "Az éjszaka sötétjében egy régi temetőben vagy. A köd leereszkedik, és szélfúvás hallatszik. Valami épp most ébredt fel.",
    [karakter_3]
)

szenario_5 = Szenario(
    "Titkos Barlang",
    "A sötét barlangban a levegő nehéz, és a csöpögő víz zajától egy hátborzongató csend telepedik a helyre. Mi lehet itt elrejtve?",
    [karakter_4, karakter_5]
)

szenario_6 = Szenario(
    "Fagyos Hegycsúcs",
    "A hegycsúcsot fagy borítja, a szél szinte átszúrja a ruházatodat. A hóviharral küzdesz, miközben feljutsz a csúcsra. Miért jöttél ide?",
    [karakter_4, karakter_5]
)

# Elérhető helyszínek listája
szenariumok = [szenario_1, szenario_2, szenario_3, szenario_4, szenario_5, szenario_6]

# Játék ciklus
while True:
    print("\nElérhető Helyszínek:")
    for idx, szenario in enumerate(szenariumok, 1):
        print(f"{idx}. {szenario.cim}")
    print("7. Kilépés a játékból")
    
    valasz = input("\nVálassz egy helyszínt a megfelelő szám begépelésével: ")
    
    if valasz == "1":
        szenario_1.belep()
    elif valasz == "2":
        szenario_2.belep()
    elif valasz == "3":
        szenario_3.belep()
    elif valasz == "4":
        szenario_4.belep()
    elif valasz == "5":
        szenario_5.belep()
    elif valasz == "6":
        szenario_6.belep()
    elif valasz == "7":
        print("Kilépés a játékból...")
        break
    else:
        print("Érvénytelen választás. Kérlek válassz egy érvényes helyszínt.")

