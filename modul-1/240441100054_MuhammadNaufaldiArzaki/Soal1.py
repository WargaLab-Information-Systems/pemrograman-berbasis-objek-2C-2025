class manusia:      
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur 
        self.alamat = alamat
        
    def berjalan(self):
        print(f"{self.nama} berjalan")
        
    def berlari(self):
        print(f"{self.nama} berlari")
        
manusia1 = manusia("Faisal","80","Bojonegoro")
manusia2 = manusia("Yoga","25","Tuban")
manusia3 = manusia("Adit","27","Pamekasan")
manusia4 = manusia("Denis","40","Ngawi")
manusia5 = manusia("Naufal","20","Sidoarjo")

manusia1.berlari()
manusia2.berjalan()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()