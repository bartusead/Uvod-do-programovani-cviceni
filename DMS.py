deg = input("Zadej stupně")
deg = int(input)

if (deg < 0) or (deg >= 360):
    print("Stupně musí být v rozsahu <0,360)")
    exit()
min = input("Zadej minuty"))
min = int(input)

if (min < 0) or (min >= 60):
    print("Minuty musí být v rozsahu <0,60)")
    exit()
sec = (input("Zadej vteřiny"))
sec = float(input)

if (sec < 0) or (sec >= 60):
    print("Vteřiny musí být v rozsahu <0,60)")
    exit()

deg_float = deg + min/60 + sec/3600    

print("Celkem",deg_float,"stupňů")


degf = input("Zadej číslo")
degf = float(input)

deg = int(degf)

minf = degf-deg

degr = degf-deg
minf = degr*60
amin = int(minf)
sec = (minf*60)%60

print("Celkem",int(input("Zadej stupně: ")) + int(input("Zadej minuty: ")/60,"stupňů")