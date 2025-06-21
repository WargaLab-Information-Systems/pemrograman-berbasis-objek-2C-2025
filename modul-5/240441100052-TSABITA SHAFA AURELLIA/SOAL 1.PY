from abc import ABC, abstractmethod

class Manusia (ABC):

    @abstractmethod
    def berbicara (self):
        pass 
    @abstractmethod
    def bekerja (self):
        pass
    @abstractmethod
    def makan (self):
        pass

class joko (Manusia):
    def berbicara(self): 
        print("joko sedang berkata : halo selamat pagi,saya joko!")
    def bekerja(self):
        print("joko bekerja sebagai kuli bangunan")
    def makan(self):
        print("joko makan nasi goreng")

class Beni (Manusia):
    def berbicara(self): 
        print("beni sedang berkata : halo, nama saya beni!")
    def bekerja(self):
        print("beni bekerja sebagai montir")
    def makan(self):
        print("beni makan soto ayam")

class Fani (Manusia):
    def berbicara(self): 
        print("fani sedang berkata : selamat malam, nama saya fani! ")
    def bekerja(self):
        print("fani bekerja sebagai guru Paud")
    def makan(self):
        print("fani makan salad buah")

class jani (Manusia):
    def berbicara(self): 
        print("jani sedang berkata : halo, nama saya jani")
    def bekerja(self):
        print("jani bekerja sebagai petani")
    def makan(self):
        print("jani makan nasi pecel")

print("=== joko ===")
manusia1 = joko()
manusia1.berbicara()
manusia1.bekerja()
manusia1.makan()

print("=== Beni ===")
manusia2 = Beni()
manusia2.berbicara()
manusia2.bekerja()
manusia2.makan()

print("=== fani ===")
manusia3 = Fani()
manusia3.berbicara()
manusia3.bekerja()
manusia3.makan()

print("=== jani ===")
manusia4 = jani()
manusia4.berbicara()
manusia4.bekerja()
manusia4.makan()