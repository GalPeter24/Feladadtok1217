import random
szamlalo=0
positiv= 0
negativ=0
szamok=[]
while szamlalo !=100:
    szam=random.randint(-100,101)
    szamok.append(szam)
    szamlalo+=1
    if szam !=0:
        if szam<0:
            positiv+=1
        else: negativ+=1
if positiv >negativ:
    print("pozitív számokból van több")
else: print('negatív számokból van több')

for szam in szamok:
    i=1 
    szam1=szamok[i]
    szam2=szamok[i+1]
    if szam1+120<szam2 or szam1-120>szam2 == szam2:
        print('van két egymás meletti szám,amelyeknek különbsége' )
    if szam > 50:
        print(szam)
        break
