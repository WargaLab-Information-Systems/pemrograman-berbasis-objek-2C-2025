class Kucing:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} berkata: miaww"

class Anjing:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} berkata: guk guk rorr"

class Burung:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} berkata: cukurukuk"


hewan_list = []
for i in range(2):
    nama_kucing = input(f"Masukkan nama kucing ke-{i + 1}: ")
    hewan_list.append(Kucing(nama_kucing))
    nama_anjing = input(f"Masukkan nama anjing ke-{i + 1}: ")
    hewan_list.append(Anjing(nama_anjing))
    nama_burung = input(f"Masukkan nama burung ke-{i + 1}: ")
    hewan_list.append(Burung(nama_burung))

print("\nSuara Hewan:")
for hewan in hewan_list:
    print(hewan.suara())