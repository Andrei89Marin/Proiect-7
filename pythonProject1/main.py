class Bloc:
    def apartamanent_1_camera(self):
        print(f'In bloc sunt apartamanente cu 1 camera')
    def apartmanent_2_camere(self):
        print(f'In bloc sunt apartamanente cu 2 camere')
    def apartament_3_camere(self):
        print(f'In bloc sunt apartamente cu 3 camere')
class Dormitor1:
   mobila = []
   electrocasnice = []
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

accesorii = Mobila()
accesorii.culoare_mobila()
accesorii.material_mobila()