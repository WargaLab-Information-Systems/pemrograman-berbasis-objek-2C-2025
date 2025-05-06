class Kucing:
    def __init__(self, nama, ras, warna, umur):
        self.nama = nama
        self.ras = ras
        self.warna = warna
        self.umur = umur
        self.jenis_hewan = "Kucing" 

    def bersuara(self):
        return "Meong!"

    def tidur(self):
        return f"{self.nama} sedang tidur di atas sofa."

    def makan(self):
        return f"{self.nama} sedang makan ikan."

    def info(self):
        return f"{self.nama} adalah {self.jenis_hewan} {self.ras} berwarna {self.warna} yang berumur {self.umur} tahun."

class Ikan:
    def __init__(self, nama, jenis, warna):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
        self.jenis_hewan = "Ikan"  

    def berenang(self):
        return f"{self.nama} sedang berenang di air."

    def makan_plankton(self):
        return f"{self.nama} sedang makan plankton."

    def bersembunyi(self):
        return f"{self.nama} bersembunyi di antara karang."

    def info(self):
        return f"{self.nama} adalah {self.jenis_hewan} {self.jenis} berwarna {self.warna}."

class Anjing:
    def __init__(self, nama, ras, warna, umur):
        self.nama = nama
        self.ras = ras
        self.warna = warna
        self.umur = umur
        self.jenis_hewan = "Anjing"  

    def bersuara(self):
        return "Guk Guk!"

    def lari(self):
        return f"{self.nama} sedang berlari di halaman."

    def menggigit(self):
        return f"{self.nama} menggigit tulang."

    def info(self):
        return f"{self.nama} adalah {self.jenis_hewan} {self.ras} berwarna {self.warna} yang berumur {self.umur} tahun."

hewan_list = [
    Kucing("kitty", "persia", "Putih", 2),
    Kucing("mochi", "anggora", "abu-abu", 1),
    Kucing("kenzy", "bengal", "oranye putih", 3),

    Ikan("nemo", "clownfish", "oranye"),
    Ikan("dory", "blue tang", "biru"), 
    Ikan("salmon","sockeye", "merah"  ),

    Anjing("doggy", "husky", "coklat", 3),
    Anjing("dog", "bulldog", "hitam", 4),
    Anjing("dudd", "akita inu", "krem", 2)
]

for hewan in hewan_list:
    print(hewan.info())
    if hewan.jenis_hewan == "Kucing":
        print(hewan.bersuara())
        print(hewan.tidur())
        print(hewan.makan())
    elif hewan.jenis_hewan == "Ikan":
        print(hewan.berenang())
        print(hewan.makan_plankton())
        print(hewan.bersembunyi())
    elif hewan.jenis_hewan == "Anjing":
        print(hewan.bersuara())
        print(hewan.lari())
        print(hewan.menggigit())
    print()  
