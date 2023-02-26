#exercitiul 1


# variabila reprezinta un element foarte important in procesul de programare
# si sunt simboluri care asociaza un nume cu o valoare

#exercitiul 2

produs = 'vin'
print(produs)
an_imbuteliat = 1980
print(an_imbuteliat)
pret = 149.76
print(pret)
demidulce = True
print(demidulce)

#exercitiul 3

print(type(produs))
print(type(an_imbuteliat))
print(type(pret))
print(type(demidulce))

# exercitiul 4
pret=round(149.76)
print(pret)

# exercitiul 5
print(f'Bautura recomandata la eveniment este {produs} datand din {an_imbuteliat}, la un super pret de {pret} de lei')
print(f'La eveniment se va consuma multe bauturi alcolice? {demidulce}')


# exercitiul 6

nume = input('nume')
prenume = input('prenume')


print(f'Numele complet are {len(nume + prenume)} caractere')

#exercitiul 7


lungime = int(input('lungime'))
latime = int(input('latime'))
aria = lungime * latime

print(f' Aria dreptunghiului este ', aria)


# exercitiul 8

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.count('the'))

#exercitiul 9

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.replace('the', 'THE'))

# exercitiul 10

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.isdigit())

