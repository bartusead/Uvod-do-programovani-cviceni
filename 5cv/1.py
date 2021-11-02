jmeno = input("Zadej jméno:\\\n")
vek = int(input(f"{jmeno}, zadej věk: "))
astr = f"Ahoj {jmeno}, {vek} let starý"
print(astr)

pattern = "{poradi}: Toto je {poradi}. iterace cyklu"
for i in range(10):
    print(pattern.format(poradi=i))

a = 1/3
print(f"1/3 = {a:.3f}")
print(a*3)


