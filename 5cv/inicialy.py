jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej příjmení: ")

inicialy = jmeno[:1] + prijmeni[:1]

print(f"Tvé iniciály jsou: {inicialy.upper()}")


y_a = "á"
osloveni = "Anežko"
soucet = 3*5
podpis = "Adam Bartůšek"

print(f"""Mil{y_a} {osloveni},
Váš výdledek je {soucet} bodů.
S pozdravem,
{podpis}""")

vypis = "{} krát {} je {}".format(3, 4, 3*4)
print(vypis)
