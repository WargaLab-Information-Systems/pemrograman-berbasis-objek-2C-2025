class Harimau:
    def __init__(self, nama, usia, berat):
        self.nama = nama
        self.usia = usia
        self.berat = berat

    def berburu(self):
        print(f"Harimau {self.nama} berburu makanan dihutan.")

    def berlari(self):
        print(f"Harimau {self.nama} berlari mengejar mangsanya.")

    def tampilkan(self):
        print(f"Nama Harimau: {self.nama}, Usia: {self.usia} Tahun, Berat: {self.berat} Kg")
        self.berburu()
        self.berlari()

class Piranha:
    def __init__(self, nama, panjang, berat):
        self.nama = nama
        self.panjang = panjang
        self.berat = berat
    
    def berenang(self):
        print(f"Ikan Piranha {self.nama} berenang dari benua Afrika ke Amerika.")

    def memakan(self):
        print(f"Ikan Piranha {self.nama} memakan ikan besar di danau.")

    def tampilkan(self):
        print(f"Nama Piranha: {self.nama}, Panjang: {self.panjang} Cm, Berat: {self.berat} Kg")
        self.berenang()
        self.memakan()

class Monyet:
    def __init__(self, nama, warna, usia):
        self.nama = nama
        self.warna = warna
        self.usia = usia
    
    def memanjat(self):
        print(f"Monyet {self.nama} memanjat pohon pisang.")

    def makan(self):
        print(f"Monyet {self.nama} memakan pisang besar.")
    
    def tampilkan(self):
        print(f"Nama Monyet: {self.nama}, Warna: {self.warna}, Usia: {self.usia} tahun.")
        self.memanjat()
        self.makan()

data_hewan = []

while True:
    input_jumlah_hewan = input("Berapa data yang ingin di-input dari setiap Class: ")
    print("-------" * 10)

    if input_jumlah_hewan.isdigit():

        input_jumlah_hewan = int(input_jumlah_hewan)
        
        for data in range(input_jumlah_hewan):
            print(f"Masukkan data Harimau ke-{data+1}")
            nama = input("Masukkan nama harimau: ")
            usia = input("Masukkan usia: ")
            berat = input("Masukkan berat: ")
            print("-------" * 10)

            harimau = Harimau(nama,usia,berat)
            data_hewan.append(harimau)
        
        for data in range(input_jumlah_hewan):
            print(f"Masukkan data Piranha ke-{data+1}")
            nama = input("Masukkan nama Piranha: ")
            panjang = input("Masukkan panjang Piranha: ")
            berat = input("Masukkan berat Piranha: ")
            print("-------" * 10)

            piranha = Piranha(nama,panjang,berat)
            data_hewan.append(piranha)

        for data in range(input_jumlah_hewan):
            print(f"Masukkan data Monyet ke-{data+1}")
            nama = input("Masukkan nama Monyet: ")
            warna = input("Masukkan warna Monyet: ")
            usia = input("Masukkan usia Monyet: ")
            print("-------" * 10)

            monyet = Monyet(nama,warna,usia)
            data_hewan.append(monyet)

        print("Data Hewan Saat ini")
        print("-------" * 10)
        for hewan in data_hewan:
            hewan.tampilkan()
            print("-------" * 10)
            
        break

    else:
        print("Input harus angka!")