deg = int(input("Zadej stupně"))


if (deg < 0) or (deg >= 360):
    print("Stupně musí být v rozsahu <0,360)")
    exit()
min = int(input("Zadej minuty"))


if (min < 0) or (min >= 60):
    print("Minuty musí být v rozsahu <0,60)")
    exit()
sec = float((input("Zadej vteřiny")))
  

if (sec < 0) or (sec >= 60):
    print("Vteřiny musí být v rozsahu <0,60)")
    exit()

deg_float = deg + min/60 + sec/3600    

print("Celkem",deg_float,"stupňů")

