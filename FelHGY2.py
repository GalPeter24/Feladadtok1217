varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]
beirt_varosnev=" "
while beirt_varosnev !="":
    beirt_varosnev=input('Add meg a városnevet!')
    if beirt_varosnev in varosok:
            i=varosok.index(beirt_varosnev)
            if varosok[-1] == beirt_varosnev:
                  print('Nincs következő!')
            else: print(varosok[i+1])
    else: varosok.append(beirt_varosnev) 
    
