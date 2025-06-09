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
        print("hello semua,kenalin aku joko")

    def bekerja(self):
        print("aku sekarang bekerja sebagai admin di sebuah perusahaan")


class Beni(Manusia):
    def berbicara(self):
        print("hello,perkenalkan saya beni")

    def bekerja(self): 
        print("saya bekerja menjadi guru di SMA")

    def makan(self):
        print("saya sangat senang sekali makan nasi goreng disaat jam istirahat")

class Fani(Manusia):
    def berbicara(self):
        print("hallo gaiss,kenalin aku fani")

    def bekerja(self):
        print("aku sekarang bekerja sebagai kasir di sebuah toko kue")

    def makan(self):
        print("aku suka makan makanan manis dan sehat")

class Jani(Manusia):
    def berbicara(self):
        print("hallo,perkenalkan nama saya jani")

    def bekerja(self):
        print("Jani bekerja sebagai arsitek")

    def makan(self):
        print("saya senang makan makanan yang sehat")

joko = Joko()
joko.berbicara()
joko.bekerja()
joko.makan()
print("-" * 30)

beni = Beni()
beni.berbicara()
beni.bekerja()
beni.makan()
print("-" * 30)

fani = Fani()
fani.berbicara()
fani.bekerja()
fani.makan()
print("-" * 30)

jani = Jani()
jani.berbicara()
jani.bekerja()
jani.makan()
