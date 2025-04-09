class Manusia: #clas
    def __init__(self, nama, umur, alamat): #constructor
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self): #method berjaklan
        return f"{self.nama} berjalan sebanyak 450.000 langkah"

    def berlari(self): #method berlari
        return f"{self.nama} berlari sejauh 11.000 KM"

#objek
manusia1 = Manusia("Ali", 21, "Kamal")
manusia2 = Manusia("Riska", 21, "Telang")
manusia3 = Manusia("Kiki", 20, "Surabaya")
manusia4 = Manusia("Gio", 19, "Bangkalan")
manusia5 = Manusia("Vano", 19, "Sidoarjo")

#menampilkan hasil
print(manusia1.berjalan())
print(manusia2.berlari())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berjalan())