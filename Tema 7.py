
'''ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi'''

from abc import abstractmethod, ABC

class FormaGeometrica(ABC):
    pi = 3.14
    R = 4
    @abstractmethod
    def aria(self):
     pass

    def descriere(self):
        print(f'Cel mai probabil am colturi')
    def __init__(self, cerc):
        self.cerc = cerc


'''INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură'''

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

patrat = Patrat(7)
print(patrat.aria())
patrat.descriere()



'''POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui'''

class Cerc(FormaGeometrica):
    def forma(self):
        print(f'Eu nu am colturi')
class Patrat (FormaGeometrica):
    def forma(self):
        print (f'Eu am colturi')

''''ENCAPSULATION'''


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura * self.__latura

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return FormaGeometrica.pi * self.__raza * self.__raza

patrat = Patrat(5)
print(patrat.latura)
patrat.latura = 6
print(patrat.aria())
patrat.descriere()

cerc = Cerc(4)
print(cerc.raza)
cerc.r = 6
print(cerc.aria())
cerc.descriere()