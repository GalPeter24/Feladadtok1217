import random
magassagok=[]
szamlalo=0
meredek=0
while szamlalo != 30:
    szam=random.randint(0,10)
    magassagok.append(szam)
    szamlalo+=1
for szam in magassagok:
    i=1
    szam1=magassagok[i]
    szam2=magassagok[i-1]
    if szam1-2>szam2 :
        meredek+1
print(meredek,'meredek út van')
print(magassagok)