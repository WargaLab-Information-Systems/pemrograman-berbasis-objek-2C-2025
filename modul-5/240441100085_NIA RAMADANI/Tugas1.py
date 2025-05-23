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
        print("Joko memiliki gaya bicara yang halus.")

    def bekerja(self):
        print("Joko bekerja sebagai Manajer di perusahaan C.")

    def makan(self):
        print("Joko suka makan sushi.")

class Beni(Manusia):
    def berbicara(self):
        print("Beni memiliki gaya bicara yang sopan.")

    def bekerja(self):
        print("Beni bekerja sebagai HRD di perusahaan B.")

    def makan(self):
        print("Beni suka makan bakso.")

class Fani(Manusia):
    def berbicara(self):
        print("Fani memiliki gaya bicara yang lembut.")

    def bekerja(self):
        print("Fani bekerja sebagai Teller di Bank BRI.")

    def makan(self):
        print("Fani suka makan seblak.")

class Jani(Manusia):
    def berbicara(self):
        print("Jani memiliki gaya bicara yang ramah.")

    def bekerja(self):
        print("Jani bekerja sebagai Sekretaris di perusahaan F.")

    def makan(self):
        print("Jani suka makan seafood.")


print("\n========== DATA MANUSIA ==========\n")

print("Profil: Joko\n")
joko = Joko()
joko.berbicara()
joko.bekerja()
joko.makan()
print("----------------------------------\n")

print("Profil: Beni\n")
beni = Beni()
beni.berbicara()
beni.bekerja()
beni.makan()
print("----------------------------------\n")

print("Profil: Fani\n")
fani = Fani()
fani.berbicara()
fani.bekerja()
fani.makan()
print("----------------------------------\n")

print("Profil: Jani\n")
jani = Jani()
jani.berbicara()
jani.bekerja()
jani.makan()
print("----------------------------------\n")
