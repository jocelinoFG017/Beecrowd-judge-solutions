n = int(input())

ins = 0
out = 0

for i in range(n):
    x = int(input())
    if(x >= 10 and x <= 20):
        ins += 1
    else:
        out += 1
print("{} in".format(ins))
print("{} out".format(out))