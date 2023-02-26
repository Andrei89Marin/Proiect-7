#exercitiul 1
#punctul a)

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)



#punctul b)

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
note_muzicale.reverse()
print(note_muzicale)

#punctul c)
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
note_muzicale[::-1]
print(note_muzicale)

#exercitiul 2
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
note_muzicale.count("do")
print(f'Avem nota do de {note_muzicale.count("do")}  ori')

#exercitiul 3

list1=[3,1,0,2]
list2=[6,5,4]
list1.extend(list2)
print(list1)

list1=[3,1,0,2]
list2=[6,5,4]
lista_noua = list1 +list2
print(lista_noua)

#exercitiul 4

lista_noua.sort()
print(f'lista sortata este {lista_noua}')

lista_noua.remove(0)
print(f'noua lista este {lista_noua}')

#exercitiul 5
x = len(lista_noua)
if x==0:
 print("Lista este goala")
else:
    print("lista are elemente in ea")

#exercitiul 6

lista_noua.clear()
print(lista_noua)

#exercitiul 7
x = len(lista_noua)
if x==0:
 print("Lista este goala")
else:
    print("lista are elemente in ea")

#exercitiul 8

dict1 = {
    "Ana" : 8,
    "Gigel" : 10,
    "Dorel" : 5
}
x = dict1.keys()
print(x)

#exercitiul 9
dict1 = {
    "Ana" : 8,
    "Gigel" : 10,
    "Dorel" : 5
}
print('Ana a luat nota:'f'{dict1["Ana"]}')
print('Gigel a luat nota:'f'{dict1["Gigel"]}')
print('Dorel a luat nota:'f'{dict1["Dorel"]}')

#exercitiul 10

dict1["Dorel"] = 6
print(dict1)

#exercitiul 11

dict1.pop("Gigel")
dict1["Ionel"]= 9
print(dict1)

#exercitiul 12

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}

zile_sapt.update('luni')
print(zile_sapt)

#exercitiul 13

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if (weekend != zile_sapt):
      print(f'zilele de {weekend} sunt in {zile_sapt}')
else:
       print(f'zilele de {weekend} nu sunt in {zile_sapt}')

#exercitiul 14
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt-weekend)

#exercitiul 15

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile = list(set(zile_sapt) & set(weekend))
print (zile)