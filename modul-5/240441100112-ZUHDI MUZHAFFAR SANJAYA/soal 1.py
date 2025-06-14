from abc import ABC, abstractmethod

# Abstract class
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

# Subclass Joko
class Joko(Manusia):
    def berbicara(self):
        print("Joko: Aku lebih suka berbicara singkat dan padat.")

    def bekerja(self):
        print("Joko: Aku bekerja sebagai petani di desa.")

    def makan(self):
        print("Joko: Aku suka makan nasi jagung dan sayur asem.")

# Subclass Beni
class Beni(Manusia):
    def berbicara(self):
        print("Beni: Saya senang berdiskusi tentang teknologi!")

    def bekerja(self):
        print("Beni: Saya bekerja sebagai programmer di perusahaan startup.")

    def makan(self):
        print("Beni: Saya paling suka makan ramen dan kopi hitam.")

# Subclass Fani
class Fani(Manusia):
    def berbicara(self):
        print("Fani: Saya suka menyapa semua orang dengan ramah.")

    def bekerja(self):
        print("Fani: Saya bekerja sebagai guru taman kanak-kanak.")

    def makan(self):
        print("Fani: Saya suka makanan sehat seperti salad dan buah-buahan.")

# Subclass Jani
class Jani(Manusia):
    def berbicara(self):
        print("Jani: Saya berbicara dengan logis dan tegas.")

    def bekerja(self):
        print("Jani: Saya seorang pengacara yang fokus membela keadilan.")

    def makan(self):
        print("Jani: Saya suka makan steak dan minum teh hijau.")

# Membuat objek dan memanggil setiap method
joko = Joko()
joko.berbicara()
joko.bekerja()
joko.makan()

beni = Beni()
beni.berbicara()
beni.bekerja()
beni.makan()

fani = Fani()
fani.berbicara()
fani.bekerja()
fani.makan()

jani = Jani()
jani.berbicara()
jani.bekerja()
jani.makan()