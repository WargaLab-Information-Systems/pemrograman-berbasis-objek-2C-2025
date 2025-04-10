class kucing:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} adalah nama kucing yang bersuara: miauuuu"

class ayam:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} adalah nama ayam yang bersuara: kukuruyuk"

class kambing:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        return f"{self.nama} adalah nama kambing yang bersuara: mbekk"

hewan_list = []

for i in range(2):
    nama_kucing = input(f"Masukkan nama kucing ke-{i + 1}: ")
    hewan_list.append(kucing(nama_kucing))
for i in range(2):  
    nama_ayam = input(f"Masukkan nama ayam ke-{i + 1}: ")
    hewan_list.append(ayam(nama_ayam))
for i in range(2):   
    nama_kambing = input(f"Masukkan nama kambing ke-{i + 1}: ")
    hewan_list.append(kambing(nama_kambing))

print("\nsuara hewan:")
for hewan in hewan_list:
    print(hewan.suara())

