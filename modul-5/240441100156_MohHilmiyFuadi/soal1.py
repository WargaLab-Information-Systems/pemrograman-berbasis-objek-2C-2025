class Manusia:
    def berbicara(self):
        pass

    def bekerja(self):
        pass

    def makan(self):
        pass

class Orang(Manusia):
    def __init__(self, nama):
        self.nama = nama
        print(f"\n=== Input untuk {self.nama} ===")
        self.kata = input(f"Apa yang ingin dikatakan {self.nama}? ")
        self.pekerjaan = input(f"Apa pekerjaan {self.nama}? ")
        self.cara_makan = input(f"Bagaimana cara {self.nama} makan? ")

    def berbicara(self):
        return f"{self.nama} berkata: {self.kata}"

    def bekerja(self):
        return f"{self.nama} bekerja sebagai {self.pekerjaan}."

    def makan(self):
        return f"{self.nama} makan dengan cara: {self.cara_makan}"

joko = Orang("Joko")
beni = Orang("Beni")
fani = Orang("Fani")
jani = Orang("Jani")

semua_data = [joko, beni, fani, jani]

print("\n=== Ringkasan Data Semua Orang ===")
for orang in semua_data:
    print(orang.berbicara())
    print(orang.bekerja())
    print(orang.makan())
    print("-" * 40)