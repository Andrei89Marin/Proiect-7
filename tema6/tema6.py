# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
class Cerc:
    raza = None
    culoare = None
    def __init__(self,raza,  culoare):
       self.raza = raza
       self.culoare = culoare
    def descriere_cerc(self):
         print(f'Raza = {self.raza} si culoarea {self.culoare}')
    def Aria(self):
         pi = 3.14
         aria = pi*self.raza**2
         return aria
    def Diametrul(self):
        diametrul = self.raza/2
        return diametrul
    def Circumferinta(self):
         pi = 3.14
         circumferinta = 2*pi*self.raza
         return circumferinta

cerc = Cerc(9,'portocaliu')
cerc.descriere_cerc()
print(cerc.Aria())
print(cerc.Diametrul())
print(cerc.Circumferinta())

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
   lungime = 0
   latime = 0
   culoare = None

   def __init__(self, lungime, latime, culoare):
         self.lungime = lungime
         self.latime = latime
         self.culoare = culoare
   def descriere(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm,latimea de {self.latime} cm si {self.culoare}')
   def aria(self):
         aria = self.lungime * self.latime
         print(aria)
   def perimetru(self):
        perimetrul = 2*self.lungime + 2*self.latime
        print(perimetrul)
dreptunghi = Dreptunghi(5, 8, "galben")
dreptunghi.descriere()
dreptunghi.aria()
dreptunghi.perimetru( )
dreptunghi.culoare = 'verde'
dreptunghi.descriere()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None
    def __init__(self,nume , prenume , salariu):
         self.nume = nume
         self.prenume = prenume
         self.salariu = salariu
    def descriere(self):
         print(f'Ma numesc {self.nume} {self.prenume} si am un salariu de {self.salariu} lei')
    def nume_complet(self):
        print(f'{self.nume} {self.prenume}')
    def salariu_lunar(self):
        print(f'Am un salariu lunar de {self.salariu}')
    def salariu_anual(self):
        salariu_anual = self.salariu*12
        print(f'Salariul anual este de {salariu_anual} lei')
    def marire_salariu(self,procent):
       self.procent = procent
       self.marire_salariu = self.salariu * self.procent/100
       self.salariu_nou = self.marire_salariu + self.salariu
       print(f'Marirea de salariu a fost cu {self.procent} % ,salariul a fost marit cu {self.marire_salariu} lei , iar acuma salariul este de {self.salariu_nou} lei')

angajat = Angajat('Andrei', 'Vasile',3500)
angajat.descriere()
angajat.nume_complet()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu(20)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
   iban = None
   titular_cont = None
   sold = None
   def __init__(self,iban, titular_cont, sold):
       self.iban = iban
       self.titular_cont = titular_cont
       self.sold = sold
   def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
   def  debitare_cont(self, suma):
       self.suma = suma
       self.debitare_cont= self.sold - self.suma
       print(f'A fost retrasa din cont suma de {self.suma} lei soldul actual este de {self.debitare_cont} lei')
   def creditare_cont(self,suma):
       self.suma = suma
       self.creditare_cont = self.sold + self.suma
       print(f'A fost adaugata in cont suma de {self.suma} lei, iar soldul actual este de {self.creditare_cont} lei')

cont = Cont(52789,'Andrei', 500)
cont.afisare_sold()
cont.debitare_cont(450)
cont.creditare_cont(957)
