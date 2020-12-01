a, b = list(map(int, input().split()))
a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
if b > a:
    if b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
if b == a:
    print("Sao Multiplos")
