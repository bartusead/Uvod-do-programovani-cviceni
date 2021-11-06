# Abych nemusel opakovat části kódu
# def jmeno_funkce (argument1, argument2):
    #
    #
    #
    # return <hodnota>

def square_area(side):
    return side*side

side = 37
area = square_area(side)
print(f"Plocha čtverce o straně {side} je {area}")


def read_int(prompt):
    astr = input(prompt)
    return int(astr)

def print_float3(num):
    print(f"{num:.3f}")


print_float3(12.3456789)
num = read_int("Zadej číslo:")
print(f"Zadal jsi {num}")


from math import pi

def circle_area(r):
    return(pi*(r*r))

r = 59
area = circle_area(r)

print(f"Obsah kruhu o poloměru {r} je {area}")


def napis_hlasku(nazev, skore):

    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', 256)
napis_hlasku('Protivníkovo', 5)

def spocitej_obsah(a, b):
    print(f"Obsah obdélníka je {a*b} metrů čtverečních")

spocitej_obsah(5,9)


def ano_nebo_ne(otazka):
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False

        print('Nerozumím! Odpověz "ano" nebo "ne".')

# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')
