#Author: Jocelino F.G

n = int(input())
print (n)

hun = int(n / 100)
fifty = int((n - hun * 100) / 50)
twen = int((n - hun * 100 - fifty * 50) / 20)
ten = int((n - hun * 100 - fifty * 50 - twen * 20) / 10)
five = int((n - hun * 100 - fifty * 50 - twen * 20 - ten * 10) / 5)
two = int((n - hun * 100 - fifty * 50 - twen * 20 - ten * 10 - five * 5) / 2)
one = int(n - hun * 100 - fifty * 50 - twen * 20 - ten * 10 - five * 5 - two * 2)

print ("{} nota(s) de R$ 100,00".format(hun))
print ("{} nota(s) de R$ 50,00".format(fifty))
print ("{} nota(s) de R$ 20,00".format(twen))
print ("{} nota(s) de R$ 10,00".format(ten))
print ("{} nota(s) de R$ 5,00".format(five))
print ("{} nota(s) de R$ 2,00".format(two))
print ("{} nota(s) de R$ 1,00".format(one))