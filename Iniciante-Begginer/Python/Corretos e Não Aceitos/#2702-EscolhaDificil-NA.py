"""
# funciona perfeitamente mas deu runtime error na plataforma
#então tive que procurar fazer de outro maneira
"""

# Refeições disponiveis
Ca = int(input())
Ba = int(input())
Pa = int(input())

# Refeições requisitadas
Cr = int(input())
Br = int(input())
Pr = int(input())

# Variaveis auxiliares
cc = 0
bb = 0
pp = 0
count = 0

if (Ca >= 0) and (Ca <= 100):
  if (Ba >= 0) and (Ba <= 100):
    if (Pa >= 0) and (Pa <= 100):      
      if (Cr >= 0) and (Cr <= 100):
        if (Br >= 0) and (Br <= 100):
          if (Pr >= 0) and (Pr <= 100):
            if Cr > Ca:
              cc = Cr-Ca
            if Br > Ba:
              bb = Br-Ba
            if Pr > Pa:
              pp = Pr- Pa
            count = cc+bb+pp
            print(count)
