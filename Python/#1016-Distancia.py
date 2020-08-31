# Está correto, porem não é aceito na URI.

import math
x1 = float(input())
x2 = float(input())

y1 = float(input())
y2 = float(input())

p1 = (x2-x1)
p2 = (y2-y1)

distance = math.sqrt((p1 * p1) + (p2 * p2))

print("%.4f" % distance)
