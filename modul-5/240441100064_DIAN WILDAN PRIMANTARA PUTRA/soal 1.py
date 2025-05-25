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
        print("Joko: Saya suka politik.")
    def bekerja(self): 
        print("Joko: Pegawai negeri.")
    def makan(self): 
        print("Joko: Makan nasi goreng.")

class Beni(Manusia):
    def berbicara(self): 
        print("Beni: Saya pendiam.")
    def bekerja(self): 
        print("Beni: Penulis buku.")
    def makan(self): 
        print("Beni: Makan mie ayam.")

class Fani(Manusia):
    def berbicara(self): 
        print("Fani: Halo semuanya!")

    def bekerja(self): 
        print("Fani: Desainer grafis.")

    def makan(self): 
        print("Fani: Makanan sehat.")

class Jani(Manusia):
    def berbicara(self): 
        print("Jani: Suka teknologi.")

    def bekerja(self): 
        print("Jani: Programmer.")
        
    def makan(self): 
        print("Jani: Makan cepat saji.")

print("=== JOKO ===")
Joko().berbicara()
Joko().bekerja()
Joko().makan()

print("\n=== BENI ===")
Beni().berbicara()
Beni().bekerja()
Beni().makan()

print("\n=== FANI ===")
Fani().berbicara()
Fani().bekerja()
Fani().makan()

print("\n=== JANI ===")
Jani().berbicara()
Jani().bekerja()
Jani().makan()