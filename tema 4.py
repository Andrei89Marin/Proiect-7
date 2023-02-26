####1.Având lista:
##mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
#Folosește un for că să iterezi prin toată lista și să afișezi;
#● ‘Mașina mea preferată este x’.
#● Fă același lucru cu un for each.
#● Fă același lucru cu un while#

#a)
masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for i in range (0, len(masina)):
     print(f'Masina mea preferata este: {masina[i]} ')

#b)

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for marca in masina:
    print(f'Masina mea preferata este: {masina}')
#c)

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
i=0
marca = len(masina)
while i<marca:
    print(f'Masina mea preferata este: {masina}')
    i=i+1

#2. Aceeași listă:
#Folosește un for else
#În for

#- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
#exceptând primul și ultimul.
#În else:
#- Printează lista.

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for i in range (0, len(masina)):
    masina[i]=masina[i].upper()
else:
    print(masina)


#3. Aceeași listă:
#Vine un cumpărător care dorește să cumpere un Mercedes.
#Itereaza prin ea prin modalitatea aleasă de tine.
#Dacă mașina e mercedes:
#Printează ‘am găsit mașina dorită de dvs’
#Ieși din ciclu folosind un cuvânt cheie care face acest lucru
#Altfel:
#Printează ‘Am găsit mașina X. Mai căutam‘


masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for marca in masina:
    if marca == "Mercedes":
        print(f'Am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {marca}. Mai cautam')

#4. Aceași listă;
#Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
#- Dacă mașina e Trabant sau Lăstun:
#Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
#- Printează S-ar putea să vă placă mașina x.

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for marca in masina:
    if marca in ["Trabant", "Lăstun"]:
        continue
print(f' S-ar putea sa va placa masina {marca}')


#5. Modernizează parcul de mașini:
#● Crează o listă goală, masini_vechi.
#● Itereaza prin mașini.
#● Când găsesti Lăstun sau Trabant:
#- Salvează aceste mașini în masini_vechi.
#- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

#● Printează Modele vechi: x.
#● Modele noi: x.

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
masina_veche = []
for marca in masina:
    if marca == 'Lăstun' or marca == 'Trabant':
        masina_veche.append(marca)
        masina.remove(marca)
        masina.append('Tesla')
print(f'Modelele vechi sunt {masina_veche}')
print(f'Modele noi sunt {masina}')

#6. Având dict:
#pret_masini = {
#'Dacia': 6800,
#'Lăstun': 500,
#'Opel': 1100,
#'Audi': 19000,
#'BMW': 23000
#}
#Vine un client cu un buget de 15000 euro.
#● Prezintă doar mașinile care se încadrează în acest buget.
#● Itereaza prin dict.items() și accesează mașina și prețul.
#● Printează Pentru un buget de sub 15000 euro puteți alege mașină
#xLastun
#● Iterează prin listă.

masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

for masina in pret_masini:
     if pret_masini.get(masina) < 15000:
         print(f'Masina care se incadreaza in buget {masina}')

for masina, pret in pret_masini.items():
     print(f'Masina {masina} si pretul {pret} ')

for masina in pret_masini:
     if pret_masini.get(masina) < 15000:
       print(f' Pentru un buget de sub 15000 euro puteți alege mașină {masina}')


#7. Având lista:
#numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#● Iterează prin ea.
#● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

i = 0
for i in numere:
    if i == 3:
        i +=1
print(f'3 apare de {i} ori')

#8. Aceeași listă:
#● Iterează prin ea
#● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for i in numere:
     sum += i
print(f'Suma numerelor din lista este {sum}')

#9. Aceeași listă:
#● Iterează prin ea.
#● Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]
for x in numere:
    if x > maxim:
       maxim=x
print(f'Numarul maxim este {maxim}')

#10. Aceeași listă:
#● Iterează prin ea.
#● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
#Ex: dacă e 3, să devină -3
#● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_noua =[]
for i in numere:
  if i>0 or i == 0:
      lista_noua.append(i*(-1))
print(lista_noua)


