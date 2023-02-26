#exercitii obligatorii

#exercitiul 1

#Conditionalul IF il folosim atunci cand avem conditii. Spre exemplu daca x= 3 printam x altfel(else) printam eroare

#exercitiul 2
x = float(input('numarul este '))
if x >= 0:
    print('numar natural')
else:
    print(' numar negativ')

# exercitiul 3

x = float(input(' numarul este'))
if x < 0:
    print('numar negativ')
elif x == 0:
    print ('numar neutru')
else:
    print ('numar pozitiv')

#exercitiul 4
x = float(input('numarul este'))
a = -2
b = 13
if x > a and x < b:
    print(f'{x} apartine interval')
else:
    print(f'{x} nu apartine interval')

#exercitiul 5

x = float(input(' primul numar este'))
y = float(input('al doilea numar este'))
z = (x-y)
if abs(z) < 5:
    print(f'diferenta dintre {x} si {y} este mai mica de 5')
elif abs(z) == 5:
    print(f'diferenta dintre {x} si {y} este egala cu 5')
else:
    print(f'diferenta dintre {x} si {y} este mai mare ca 5')

#exercitiul 6
x = int(input('numarul este'))
if not (5<= x <=27):
    print(f'{x} nu apartine intervalului')
else:
    print(f'{x} apartine intervalului')

#exercitiul 7
x = int(input('primul numar este'))
y = int(input('al doilea numar este'))
if x==y:
    print(f'{x} este egal cu {y}')
elif x < y:
    print(f'{x} este mai mic ca {y}')
else:
    print (f'{x} este mai mare ca {y}')

#exercitiul 8
x = int(input('prima latura are lungimea de'))
y = int(input('a doua latura are lungimea de'))
z = int(input('a treia latura are lungimea de'))
if x==y==z:
    print(f'Triunghiul este echilateral')
elif (x==y or x==z or z==x):
    print(f'Triunghiul este isoscel')
else:
    print(f'Triunghiul este oarecare')

#exercitiul 9

x = str(input('introdu o litera'))
y = 'AaEeIiOoUu'
if x in y:
    print(f'{x} este vocala')
else:
    print(f'{x} nu este vocala')

#exercitiul 10
nota=float(input('Nota in sistemul romanesc este'))
if 9 < nota <= 10:
    print(f' Ai luat nota A echivalent cu  {nota} in sitem romanesc')
elif 8 < nota <= 9:
    print(f' Ai luat nota B echivalent cu  {nota} in sitem romanesc')
elif 7 < nota <= 8:
    print(f' Ai luat nota C echivalent cu  {nota} in sitem romanesc')
elif 6 < nota <= 7:
    print(f' Ai luat nota D echivalent cu  {nota} in sitem romanesc')
elif 4 < nota <= 6:
    print(f' Ai luat nota E echivalent cu  {nota} in sitem romanesc')
else:
    print(f' Ai luat nota F echivalent cu  {nota} in sitem romanesc')