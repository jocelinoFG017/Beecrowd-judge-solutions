# Author: Jocelino F.G.

t = int(input())
n = []
j = 0
for i in range(0, 1000):
    n.append(j)
    print("N[{}] = {}".format(i, j))
    if (t >= 2) and (t <= 50):
        if j < t-1:
            j += 1
        else:
            j == t-1
            j = 0
