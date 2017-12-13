from random import randint

def vahemik(x,y):
    return randint(x,y)

xvahemik = int(input("Sisestage minimaalne arv, mida arvuti mõtleks:"))
yvahemik = int(input("Sisestage maksimaalne arv, mida arvuti mõtleks:"))


while True:
    a = vahemik(xvahemik, yvahemik)
    arvamine = int(input("Arvake ära, mis numbri ma mõtlesin [%d - %d]: "%(xvahemik, yvahemik)))
    print(a)
    if a == arvamine:
            valik = input("Arvasite õigesti! Kas soovite edasi mängida? [Jah], [Ei]: ")
            if valik == "Jah" or valik == "jah":
                continue
            elif valik == "Ei" or valik == "ei":
                break
            else:
                print("Sellist valikut polnud, mäng läheb kinni.")
                break
    while arvamine != a:
        if a == arvamine:
            valik = input("Arvasite õigesti! Kas soovite edasi mängida? [Jah], [Ei]: ")
            if valik == "Jah" or valik == "jah":
                continue
            elif valik == "Ei" or valik == "ei":
                break
            else:
                print("Sellist valikut polnud, mäng läheb kinni.")
                break
        elif arvamine < a and arvamine != a:
            print("Minu arv on suurem.")
            arvamine = int(input("Arvake uuesti: "))
            if a == arvamine:
                valik = input("Arvasite õigesti! Kas soovite edasi mängida? [Jah], [Ei]: ")
                if valik == "Jah" or valik == "jah":
                    continue
                elif valik == "Ei" or valik == "ei":
                    break
                else:
                    print("Sellist valikut polnud, mäng läheb kinni.")
                    break
        elif arvamine > a and arvamine != a:
            print("Minu arv on väiksem.")
            arvamine = int(input("Arvake uuesti: "))
            if a == arvamine:
            valik = input("Arvasite õigesti! Kas soovite edasi mängida? [Jah], [Ei]: ")
                if valik == "Jah" or valik == "jah":
                    continue
                elif valik == "Ei" or valik == "ei":
                    break
                else:
                    print("Sellist valikut polnud, mäng läheb kinni.")
                    break
        
    