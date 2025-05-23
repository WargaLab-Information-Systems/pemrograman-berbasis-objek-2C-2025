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
        print("Belajarlah dengan hati, bukan hanya untuk nilai. Gagal itu wajar, yang penting terus mencoba dan jangan pernah berhenti bermimpi")

    def bekerja(self):
        print("Joko bekerja sebagai Guru.")

    def makan(self):
        print("Joko sedang makan bakso.")

class Beni(Manusia):
    def berbicara(self):
        print("Ngoding itu seni... seni menyulap error jadi fitur!")

    def bekerja(self):
        print("Beni bekerja sebagai Programmer.")

    def makan(self):
        print("Beni makan buah setiap sore.")

class Fani(Manusia):
    def berbicara(self):
        print("Mencegah lebih baik daripada mengobati. Jaga diri, jaga hidupmu.")

    def bekerja(self):
        print("Fani bekerja sebagai Dokter.")

    def makan(self):
        print("Fani makan makanan sehat setiap hari.")    

class Jani(Manusia):
    def berbicara(self):
        print("Ide bagus datang dari rasa ingin tahu yang tak pernah puas.")

    def bekerja(self):
        print("Jani bekerja sebagai Desainer.")

    def makan(self):
        print("Jani makan nasi, lauknya kreativitas.")   

joko = Joko()
joko.berbicara()
joko.bekerja ()
joko.makan()

print()

beni = Beni()
beni.berbicara()
beni.bekerja ()
beni.makan()

print()

fani = Fani()
fani.berbicara()
fani.bekerja ()
fani.makan()

print()

jani = Jani()
jani.berbicara()
jani.bekerja ()
jani.makan()

