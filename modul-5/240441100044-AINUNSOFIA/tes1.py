from abc import ABC, abstractmethod

class manusia(ABC):

    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

# subclass joko
class joko(manusia):
    def berbicara(self):
        print("joko berbicara menggunakan bahasa jawa")

    def bekerja(self):
        print("joko bekerja sebagai kuli bangunan")

    def makan(self):
        print("joko biasanya makan nasi pecel")

# subclass beni
class beni(manusia):
    def berbicara(self):
        print("beni berbicara menggunakan bahasa madura")

    def bekerja(self):
        print("beni bekerja di pasar")

    def makan(self):
        print("beni makan nasi jagung")

# subclass fani
class fani(manusia):
    def berbicara(self):
        print("fani berbicara sesuai moodnya")

    def bekerja(self):
        print("fani bekerja sebagai penjual pecel")

    def makan(self):
        print("fani makannya ya nasi pecel siii")

# subclass jani
class jani(manusia):
    def berbicara(self):
        print("jani berbicara menggunakan mulut")

    def bekerja(self):
        print("jani bekerja sebagai tukang parkir")

    def makan(self):
        print("jani sedang makan pop mie")

# object
jk = joko()
jk.berbicara()
jk.bekerja()
jk.makan()
print("\n")
bn = beni()
bn.berbicara()
bn.bekerja()
bn.makan()
print("\n")
fn = fani()
fn.berbicara()
fn.bekerja()
fn.makan()
print("\n")
jn = jani()
jn.berbicara()
jn.bekerja()
jn.makan()