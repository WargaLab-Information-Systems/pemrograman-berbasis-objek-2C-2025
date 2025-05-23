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
        print("Joko : Saya bicara dengan klien")
        
    def bekerja(self):
        print("Joko : Saya bekerja sebagai arsitektur")
        
    def makan(self):
        print("Joko : Saya makan indomie")
        
class Beni(Manusia):
    def berbicara(self):
        print("Beni : Saya bicara tentang perusahaan")
        
    def bekerja(self):
        print("Beni : Saya bekerja sebagai manager")
        
    def makan(self):
        print("Beni : Saya makan nasi goreng")
        
class Fani(Manusia):
    def berbicara(self):
        print("Fani : Saya bicara dengan pelamar kerja")
        
    def bekerja(self):
        print("Fani : Saya bekerja sebagai hrd")
        
    def makan(self):
        print("Fani : Saya makan soto")
        
class Jani(Manusia):
    def berbicara(self):
        print("Jani : Saya bicara tentang bisnis")
        
    def bekerja(self):
        print("Jani : Saya bekerja sebagai wirausaha")
        
    def makan(self):
        print("Jani : Saya makan mie ayam")
        
Joko = Joko()
Joko.berbicara()
Joko.bekerja()
Joko.makan()
print()

Beni = Beni()
Beni.berbicara()
Beni.bekerja()
Beni.makan()
print()

Fani = Fani()
Fani.berbicara()
Fani.bekerja()
Fani.makan()
print()

Jani = Jani()
Jani.berbicara()
Jani.bekerja()
Jani.makan()
print()