from abc import ABC, abstractmethod
class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass
    @abstractmethod
    def bekerja(self):
        pass
    @abstractmethod
    def makan(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        print("Halo, apa kabar?")
    def bekerja(self):
        print("Joko bekerja di bengkel.")
    def makan(self):
        print("Joko makan nasi campur.")

class Beni(Manusia):
    def berbicara(self):
        print("Kabarku baik.")
    def bekerja(self):
        print("Beni bekerja sebagai guru.")
    def makan(self):
        print("Beni makan ayam geprek.")

class Fani(Manusia):
    def berbicara(self):
        print("Aku lapar.")
    def bekerja(self):
        print("Fani bekerja sebagai tukang service AC.")
    def makan(self):
        print("Fani makan mie ayam.")

class Jani(Manusia):
    def berbicara(self):
        print("Ayo kita makan!")
    def bekerja(self):
        print("Jani bekerja di perusahaan.")
    def makan(self):
        print("Jani makan indomie.")

joko = Joko()
beni = Beni()
fani = Fani()
jani = Jani()

joko.bekerja()
beni.bekerja()
fani.bekerja()
jani.bekerja()
print()

joko.berbicara()
beni.berbicara()
fani.berbicara()
jani.berbicara()
print()

joko.makan()
beni.makan()
fani.makan()
jani.makan()