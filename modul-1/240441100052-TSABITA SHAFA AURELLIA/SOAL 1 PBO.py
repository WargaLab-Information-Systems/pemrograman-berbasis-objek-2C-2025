class  Manusia:
    def __init__(self,nama,umur,alamat):
        self.nama = nama 
        self.umur = umur
        self.alamat = alamat
    def berjalan (self):
        print (f"{self.nama,}sedang berjalan.") 
    def berlari (self):
        print (f"{self.nama,}sedang berlari.")
    
manusia1= Manusia("tsabita",18,"lamongan")
manusia2 =Manusia("lia",15,"lampung")
manusia3= Manusia("adit",16,"bandung")
manusia4= Manusia("rafa",18,"jakbar")
manusia5= Manusia("jihan",17,"medan")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()
