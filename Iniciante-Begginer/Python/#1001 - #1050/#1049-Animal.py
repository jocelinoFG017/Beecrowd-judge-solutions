words = [0,0,0]
x = 0
while x <= 2:
    words[x] = input()
    x = x + 1
if words[0] == "vertebrado":
    if words[1] == "ave":
        if words[2] == "carnivoro":
            print("aguia")
        if words[2] == "onivoro":
            print("pomba")
    if words[1] == "mamifero":
        if words[2] == "onivoro":
            print("homem")
        if words[2] == "herbivoro":
            print("vaca")
if words[0] == "invertebrado":
    if words[1] == "inseto":
        if words[2] =="hematofago":
            print("pulga")
        if words[2] =="herbivoro":
            print("lagarta")
    if words[1] == "anelideo":
        if words[2] =="hematofago":
            print("sanguessuga")
        if words[2] == "onivoro":
            print("minhoca")