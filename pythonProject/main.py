class Dormitor1:

   def mobila(self):
       print(f'Dormitorul 1 are mobila')

   def electrocasnice(self):
       print (f'Dormitorul 1 are electrocasnice')

class Mobila(Dormitor1):

    def culoare_mobila(self):
     print(f'Mobila are culoarea negru')

    def material_mobila(self):
        print(f'Mobila este facut din mdf ')

camera = Dormitor1()
camera.mobila()
camera.electrocasnice()
accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()

class Dormitor2:

   def mobila(self):
       print(f'Dormitorul 2 este mobilat')

   def electrocasnice(self):
       print (f'Dormitorul 2 nu are electrocasnice')

class Mobila(Dormitor2):

    def culoare_mobila(self):
     print(f'Mobila are culoarea maro')

    def material_mobila(self):
        print(f'Mobila este facut din pal')

camera = Dormitor2()
camera.mobila()
camera.electrocasnice()
accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()

class Living:

   def mobila(self):
       print(f'Livingul este mobilat')

   def electrocasnice(self):
       print (f'Livingul are televizor cu diagonala 126 cm')

class Mobila(Living):

    def culoare_mobila(self):
     print(f'Mobila are culoarea wange')

    def material_mobila(self):
        print(f'Mobila este facut din pal si mdf')

camera = Living()
camera.mobila()
camera.electrocasnice()
accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()

class Bucatarie:

   def mobila(self):
       print(f'Bucataria este complet mobilata')

   def electrocasnice(self):
       print (f'Bucataria este complet utilata')

class Mobila(Bucatarie):

    def culoare_mobila(self):
     print(f'Mobila are culoarea gri')

    def material_mobila(self):
        print(f'Mobila este facut din mdf')

camera = Bucatarie()
camera.mobila()
camera.electrocasnice()
accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()

class Baie:

   def mobila(self):
       print(f'Baia este mobilata')

   def obiecte_sabitare(self):
       print (f'Baia are toate obiectele sanitare functionale')

class Mobila(Baie):

    def culoare_mobila(self):
     print(f'Mobila are culoarea alb')

    def material_mobila(self):
        print(f'Mobila este facut din lemn masiv')

camera = Baie()
camera.mobila()
camera.obiecte_sabitare()
accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()

class Apartament:

   def etaj(self):
       print(f'Apartamentul este situat la etajul 5')

   def numar(self):
       print (f'Apaartamentul are numarul 20')

class Pozitie(Apartament):

    def orientare(self):
     print(f'Apartamentul este situat cu fata la soare')

    def asezare(self):
        print(f'Apartamentul este situat cu vedere la parc')

apartament = Apartament()
apartament.etaj()
apartament.numar()

orientare = Pozitie()
orientare.orientare()
orientare.asezare()