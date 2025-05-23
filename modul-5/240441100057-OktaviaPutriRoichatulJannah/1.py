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
        print("Joko berbicara dengan tulus dari hati")

    def bekerja(self):
        print("Joko bekerja untuk melanjutkan hidup")

    def makan(self):
        print("Joko makan tiga kali sehari")


class Beni(Manusia):
    def berbicara(self):
        print("Beni berbicara sesuka hatinya")

    def bekerja(self):
        print("Beni bekerja lembur setiap hari")

    def makan(self):
        print("Beni makan nasi setiap hari")


class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara setiap saat tanpa henti")

    def bekerja(self):
        print("Fani bekerja di perusahaan besar")

    def makan(self):
        print("Fani hanya makan telur rebus setiap pagi")


class Jani(Manusia):
    def berbicara(self):
        print("Jani hanya berbicara saat butuh saja")

    def bekerja(self):
        print("Jani bekerja di toko bunga")

    def makan(self):
        print("Jani makan semua jenis makanan")


print()
print("=" * 40)
print()
print("  OUTPUT YANG DIHASILKAN DARI PROGRAM")
print()
print("=" * 40)
print()


jk = Joko()
jk.berbicara()
jk.bekerja()
jk.makan()

print()
print("=" * 40)
print()

bn = Beni()
bn.berbicara()
bn.bekerja()
bn.makan()

print()
print("=" * 40)
print()

fn = Fani()
fn.berbicara()
fn.bekerja()
fn.makan()

print()
print("=" * 40)
print()

jn = Jani()
jn.berbicara()
jn.bekerja()
jn.makan()


