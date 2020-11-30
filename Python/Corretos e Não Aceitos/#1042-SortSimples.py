x = [0,0,0,0]
x[0] = int(input())
x[1] = int(input())
x[2] = int(input())

n1 = x[0]
n2 = x[1]
n3 = x[2]

if (n1 <= n2) and (n2 <= n3):
    print("\n",n1,"\n",n2,"\n",n3)
elif (n1 <= n3) and (n3 <= n2):
    print("\n",n1,"\n",n3,"\n",n2)
elif (n2 <= n1) and (n1 <= n3):
    print("\n",n2,"\n",n1,"\n",n3)
elif (n2 <= n3) and (n3 <= n1):
    print("\n",n2,"\n",n3,"\n",n1)
elif (n3 <= n1) and (n1 <= n2):
    print("\n",n3,"\n",n1,"\n",n2)
else:
    print(n3,"\n",n2,"\n",n1)

print("\n",n1,"\n",n2,"\n",n3)



