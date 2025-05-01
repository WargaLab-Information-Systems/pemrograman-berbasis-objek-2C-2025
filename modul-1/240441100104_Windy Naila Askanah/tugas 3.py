class anjing:
    def __init__(self, nama): 
        self.nama = nama

    def suara(self): 
        print(f"{self.nama} mengeluarkan suara gonggongan")

class sapi:
    def __init__(self, nama): 
        self.nama = nama

    def suara(self): 
        print(f"{self.nama} mengeluarkan suara moo")
 
class bebek:
    def __init__(self, nama): 
        self.nama = nama

    def suara(self): 
        print(f"{self.nama} mengeluarkan suara kwek kwek")

n = int(input("Berapa hewan per jenis? "))

print("\n=== ANJING ===")
for i in range(n):
    nama = input(f"Nama anjing {i+1}: ")
    anjing(nama).suara()

print("\n=== SAPI ===")
for i in range(n):
    nama = input(f"Nama sapi {i+1}: ")
    sapi(nama).suara()

print("\n=== bebek ===")
for i in range(n):
    nama = input(f"Nama bebek {i+1}: ")
    bebek(nama).suara()