#1.Funcție care să calculeze și să returneze suma a două numere

def sum(a, b):
    return a+b
print(sum(9, 5));

#2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numar_par_impar(numar=True):
    if numar % 2 == 0:
        print(f' TRUE');
    else:
        print(f'false');
numar_par_impar(7)

#3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

def caractere_numele_meu(nume, prenume, nume_mijlociu):
    litere_nume_meu = len(nume) + len(prenume) + len(nume_mijlociu)
    return(litere_nume_meu)
print(f'Numarul total de caractere: {caractere_numele_meu("Marin", "Andrei", "Ionut")}')

#4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(l, L):
    aria = L*l;
    return aria
print(f'Aria dreptunghiului este {aria_dreptunghiului(9,7)}');

#5. Funcție care returnează aria cercului

def aria_cercului(R):
    pi = 3.14;
    aria = pi*R**2;
    return aria
print(f'Aria cercului este: {aria_cercului(7)}')

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește

def caracter(cuvant):
    if 'a' in cuvant:
        return True
    else:
        return False
print(caracter('alabala'))
print(caracter('xilofon'))

#7. Funcție fără return, primește un string și printează pe ecran:
#● Nr de caractere lower case este x
#● Nr de caractere upper case exte y

def sir(cuvant):
    i = 0
    j = 0
    for caracter in cuvant:
        if caracter.islower():
            i+=1
        else:
            j+=1
    print(f'Avem {j} caractere mari')
    print(f'Avem {i} caractere mici')
print(sir('CaTelus'))

#8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
def lista_numere( *numere):
    lista = []
    for n in numere:
        if n > 0:
            lista.append(n)
    return lista
print(lista_numere(-7,6 ,9,-4,6,78,-10))

#9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
#● Primul număr x este mai mare decat al doilea nr y
#● Al doilea nr y este mai mare decat primul nr x
#● Numerele sunt egale.

def comparatie_numere(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare ca al doilea numar {y}')
    elif y > x:
        print (f'Al doilea numar {y} este mai mare ca primul numar {x}')
    else:
        print (f' Primul numar {x} este egal cu al doilea numar {y}')
print(comparatie_numere(7,8))


#10.Funcție care primește un număr și un set de numere.
#● Printeaza ‘am adaugat numărul nou în set’ + returnează True
#● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False


def sir_numar(numar,set_de_numere):
    if numar not in set_de_numere:
        set_de_numere = set_de_numere.append(numar)
        print('am adaugat numărul nou în set')
        return True
    else:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False
print(sir_numar(9,[8,4,78,94,65]))
