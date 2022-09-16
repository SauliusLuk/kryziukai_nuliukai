lentele = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]

zaidejas = "X"
laimetojas = None
zaidimas = True


def spausdinti_lentele(lentele):
    print(lentele[6] + '|' + lentele[7] + '|' + lentele[8] + '    7|8|9')
    print(lentele[3] + '|' + lentele[4] + '|' + lentele[5] + '    4|5|6')
    print(lentele[0] + '|' + lentele[1] + '|' + lentele[2] + '    1|2|3')

# zaidejas iveda ejima
def zaidejo_ejimas(lentele):  # zaidejo ejimas bus irasytas (lenteleje)
    ivesti = int(input("Enter a number 1-9: "))  # paversti input i integer, kadangi input bus string
    if ivesti >= 1 and ivesti <= 9 and lentele[ivesti -1] == "-":  # leidzia ivesti skaiciu 1-9, patikrinam ar pasirinktoj pozicijoj lenteleje yra "-"
        lentele[ivesti -1] = zaidejas  # priskiriame pasirinkta pozicija zaidejui (klaviaturos skaicius minus 1)
    else:
        print("Negalima pasirinkti sito lauko, bandykite dar kart")


# patikrinti laimetoja
def ar_laimejo(lentele):
    global laimetojas
    if lentele[0] == lentele[1] == lentele[2] and lentele[0] != "-":
        laimetojas = lentele[0]
        return True
    elif lentele[3] == lentele[4] == lentele[5] and lentele[3] != "-":
        laimetojas = lentele[3]
        return True
    elif lentele[6] == lentele[7] == lentele[8] and lentele[6] != "-":
        laimetojas = lentele[6]
        return True
    elif lentele[0] == lentele[3] == lentele[6] and lentele[0] != "-":
        laimetojas = lentele[1]
        return True
    elif lentele[1] == lentele[4] == lentele[7] and lentele[1] != "-":
        laimetojas = lentele[1]
        return True
    elif lentele[2] == lentele[5] == lentele[8] and lentele[2] != "-":
        laimetojas = lentele[2]
        return True
    elif lentele[0] == lentele[4] == lentele[8] and lentele[0] != "-":
        laimetojas = lentele[0]
        return True
    elif lentele[2] == lentele[4] == lentele[6] and lentele[2] != "-":
        laimetojas = lentele[2]
        return True

#patikrinti lygiasias
def ar_lygiosios(lentele):
    global zaidimas
    if "-" not in lentele:  # jei lenteleje nebeliko "-", lygiosios
        spausdinti_lentele(lentele)
        print("Lygiosios!")
        zaidimas = False  # sustabdome zaidima


def kas_laimetojas():  # patikrinam ar anksciau isvardintos salygos atitinka laimejimo kriterijus
    global zaidimas
    if ar_laimejo(lentele):
        print(f"\nLaimetojas zaidejas {laimetojas}\n")
        print(f"Žaidimo rezultatas:")
        spausdinti_lentele(lentele)
        zaidimas = False


# kito zaidejo ejimas
def keisti_zaideja():
    global zaidejas
    if zaidejas == "X":  # jei dabartinis zaidejas yra X
        zaidejas = "0"  # pakeiciame zaideja i O.
    else:
        zaidejas = "X"  # jei dabartinis zaidejas nera X, duoti ejima X


while zaidimas:
    spausdinti_lentele(lentele)  # atspausdinsim lentele
    zaidejo_ejimas(lentele)
    kas_laimetojas()
    ar_lygiosios(lentele)
    keisti_zaideja()
