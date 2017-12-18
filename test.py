inimesed = int(input("Mitu inimest on kokku: "))
kohad = int(input("Mitu kohta on bussis: "))

bussid = inimesed // kohad
viimases = inimesed % kohad

if viimases == 0:
    print("Kokku on busse %d ja viimases on %d."%(bussid, inimesed))
elif viimases != 0:
    print("Kokku on busse %d ja viimases on %d"%(bussid + 1, viimases))