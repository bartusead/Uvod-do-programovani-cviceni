slovo = input("Zadej slovo: ")
pozice = int(input("Kolikáté písmeno chceš zaměnit?: "))
novy_znak = input("Zadej nové písmeno: ")

zacatek_slova = slovo[:pozice]
konec_slova = slovo[pozice + 1:]
nove_slovo = zacatek_slova + novy_znak + konec_slova

print(nove_slovo)