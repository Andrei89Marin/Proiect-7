lista_jucatori_teren = [ "Andrei", "Vasile", "George", "Ion", "Alex"]
lista_jucatori_rezerva = ["Mihai", "Marius", "Paul", "Ionut","Sebi"]
lista_jucatori_scosi = []
schimbari_efectuate = 0
schimbari_max = 3
schimbari_disponibile = schimbari_max - schimbari_efectuate

jucator_schimbat = input(' Jucatorul care urmeaza sa fie schimbat: ')
jucator_nou = input (' Jucatorul care urmeaza sa intre in teren: ')

if jucator_schimbat in lista_jucatori_teren and jucator_nou in lista_jucatori_rezerva and jucator_nou not in lista_jucatori_teren and schimbari_disponibile > 0:
    lista_jucatori_teren.remove(jucator_schimbat)
    lista_jucatori_scosi.append(jucator_schimbat)
    lista_jucatori_teren.append(jucator_nou)
    lista_jucatori_rezerva.remove(jucator_nou)
    schimbari_efectuate = schimbari_efectuate + 1
    schimbari_disponibile = schimbari_max - schimbari_efectuate
    print(f' A intrat in teren {jucator_nou}, a iesit din teren {jucator_schimbat} si mai aveti {schimbari_disponibile} schimbari disponibile')
elif jucator_nou not in lista_jucatori_rezerva or jucator_nou in lista_jucatori_teren:
    print(f'Nu se poate realiza schimabrea deoarece {jucator_nou} se afla in teren sau {jucator_nou} nu se afla pe banca de rezerva')
    print(f'Mai aveti {schimbari_disponibile} schimbari disponibile')
elif schimbari_disponibile == 0:
    print('Nu mai avem schimbari disponibile')
else:
    print(f'{jucator_schimbat} nu este in teren')
    print(f'{schimbari_disponibile} schimbari disponibile')

print(f'Jucatori in teren {lista_jucatori_teren}')
print(f'Jucatori pe banca de rezerva {lista_jucatori_rezerva}')
print(f'Jucatori folositi {lista_jucatori_scosi}')
print(f'Schimabri posibile {schimbari_disponibile}')
print(f'Schimbarile efectuate {schimbari_efectuate}')