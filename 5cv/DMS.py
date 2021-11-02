

sirka = input("Zadej stupně, minuty a vteřiny zeměpisné šířky:")
smer = (sirka[0:1])
stupne = int(sirka[1:4])
minuty = int(sirka[6:8])
vteriny = float(sirka[10:-1])

print(smer, stupne, minuty, vteriny)

cislo = stupne + minuty/60 + vteriny/3600

print(f"stupně: {smer}0{cislo:.5f}")







