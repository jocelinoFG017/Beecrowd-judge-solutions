n = int(input())
count = 0
for i in range(1, (n*4)+1):
    count += 1
    if count % 4 != 0:
        print(i, end=' ')
    else:
        print("PUM")
