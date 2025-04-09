class Kelinci: #class hewan 1
    def __init__(self, nama, umur, warna): #constructor
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def info_kelinci(self): #method
        return f"{self.nama} adalah seekor kelinci berumur {self.umur} tahun, bulunya berwarna {self.warna}"

class Kucing:  #class hewan 2
    def __init__(self, nama, umur, warna): #constructor
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def info_kucing(self): #method
        return f"ini kucingku namanya {self.nama}, umrunya {self.umur} tahun, bulunya berwarna {self.warna}"

class Hamster:  #class hewan 3
    def __init__(self, nama, umur, warna): #constructor
        self.nama = nama
        self.umur = umur
        self.warna = warna

    def info_hamster(self): #method
        return f"hewan ini memiliki warna {self.warna}, umurnya baru {self.umur} bulan, panggilannya {self.nama}"

#list untuk menyimpan 3 objek
hewan_list = [
    Kelinci("yuyu", 1 , "putih mix hitam"),
    Kelinci("gigi", 1, "hitam"),
    Kelinci("kiyo", 1, "abu-abu"),
    
    Kucing("asep", 1, "hitam mix abu"),
    Kucing("awan", 2, "putih bulux"),
    Kucing("ririmu", 1, "orange"),
    
    Hamster("err", 4, "coklat"),
    Hamster("fla", 2, "putih"),
    Hamster("tije", 3, "coklat"),
]

#looping untuk menampilkan hasil
for hewan in hewan_list:
    if isinstance(hewan, Kelinci):
        print(hewan.info_kelinci())
    elif isinstance(hewan, Kucing):
        print(hewan.info_kucing())
    elif isinstance(hewan, Hamster):
        print(hewan.info_hamster())
