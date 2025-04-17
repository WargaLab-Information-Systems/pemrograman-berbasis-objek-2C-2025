class kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def suara(self):
        return "miaww"

    def info(self):
        print(f"Kucing : {self.nama}")
        print(f"Umur   : {self.umur} tahun")

class anjing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def suara(self):
        return "guk-guk-gukk"

    def info(self):
        print(f"Anjing : {self.nama}")
        print(f"Umur   : {self.umur} tahun")

class burung:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def suara(self):
        return "cicit-cicuittt"

    def info(self):
        print(f"Burung : {self.nama}")
        print(f"Umur   : {self.umur} tahun")

kucing_list = []
anjing_list = []
burung_list = []

print("------Data Kucing------")
for i in range(3):
    nama = input("Masukkan nama kucing: ")
    umur = input("Masukkan umur kucing: \n")
    kucing_list.append(kucing(nama, umur))

print("------Data Anjing------")
for i in range(3):
    nama = input("Masukkan nama anjing: ")
    umur = input("Masukkan umur anjing: \n")
    anjing_list.append(anjing(nama, umur))

print("------Data Burung------")
for i in range(3):
    nama = input("Masukkan nama burung: ")
    umur = input("Masukkan umur burung: \n")
    burung_list.append(burung(nama, umur))

print("---------------------")
for kcng in kucing_list:
    kcng.info() 
    print(f"Suara  : {kcng.suara()}\n")
print("---------------------")
for ajg in anjing_list:
    ajg.info()
    print(f"Suara  : {ajg.suara()}\n")
print("---------------------")
for brng in burung_list:
    brng.info()
    print(f"Suara  : {brng.suara()}\n")