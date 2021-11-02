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


