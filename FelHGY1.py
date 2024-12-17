szamlalo=0
legtobb_space_mondat= 'a'
legtobb_space=0
while szamlalo !=5:
    valasz= input('Írsz be egy mondatot!')
    space_szamlalo= 0
    for karakter in valasz:
        if karakter == " ":
            space_szamlalo+=1
    if space_szamlalo > legtobb_space:
        legtobb_space= space_szamlalo
        legtobb_space_mondat=valasz
    szamlalo+=1

print('Ebben a mondatbab volt a legtöbb szóköz: ',legtobb_space_mondat)