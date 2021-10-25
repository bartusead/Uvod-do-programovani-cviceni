from random import randrange

cislo = randrange(10)

hadac = int(input("Hádej číslo:"))

while(cislo != hadac):
    if hadac < cislo:
        print("Špatně, zkus vyšší číslo, musíš přičíst", cislo-hadac)
        hadac = int(input("Hádej číslo:")) 
    elif hadac > cislo:
        print("Špatně, zkus nižší číslo, musíš odečíst", hadac-cislo)
        hadac = int(input("Hádej číslo:")) 

else:
    print("Správně")
    exit()
    
# git init - vytvoří repozitář
# git status - zobrazí stav repozitáře
# git add - přidá soubory do věcí ke commitu
# git commit - potvrdí změny
# git log - zobrazí historii

