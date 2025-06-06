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
        print("Joko berbicara dengan tenang dan penuh pertimbangan")

    def bekerja(self):
        print("Joko bekerja sebagai petani di desa.")

    def makan(self):
        print("Joko makan dengan lahap setelah bekerja di ladang.")

class Beni(Manusia):
    
    def berbicara(self):
        print("Beni berbicara cepat dan antusias.")

    def bekerja(self):
        print("Beni bekerja sebagai pengembang perangkat lunak.")

    def makan(self):
        print("Beni suka mencoba makanan baru di kafe modern.")

class Fani(Manusia):
    
    def berbicara(self):
        print("Fani berbicara lembut dan penuh empati.")

    def bekerja(self):
        print("Fani bekerja sebagai guru di sekolah dasar.")

    def makan(self):
        print("Fani lebih suka makanan sehat dan bergizi.")

class Jani(Manusia):
    
    def berbicara(self):
        print("Jani berbicara dengan gaya yang humoris.")

    def bekerja(self):
        print("Jani bekerja sebagai seniman jalanan.")

    def makan(self):
        print("Jani suka makan sambil mendengarkan musik.")


joko = Joko()
joko.berbicara()
joko.bekerja()
joko.makan()
print("-" * 40)

beni = Beni()
beni.berbicara()
beni.bekerja()
beni.makan()
print("-" * 40)

fani = Fani()
fani.berbicara()
fani.bekerja()
fani.makan()
print("-" * 40)

jani = Jani()
jani.berbicara()
jani.bekerja()
jani.makan()
print("-" * 40)