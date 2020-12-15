n = int(input())

for i in range(n):
    lista = list(map(float,input().split()))
    a2,b3,c5 = lista
    a2 = a2 * 2
    b3 = b3 * 3
    c5 = c5 * 5
    MediaPonderada = (a2 + b3 + c5)/10.0
    print("{:.1f}".format(MediaPonderada))