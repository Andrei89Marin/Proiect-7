#exercitiul 1
x = input('nume')
print(x[len(x)//2])

#exercitiul 2

x= input('ele fac cafele')
if (x==x[::-1]):
    print('true')
else:
    print('false')

#exercitiul 3

a,b = input('nume'), input('nume1')
print(a,b)

#exercitiul 4

#exercitiul 5

y = input('user: ')
b = input ('parola: ')
c= len(b)
print(f"Parola pentru user {y}, este {c * 'x'}  si are {c} caractere")