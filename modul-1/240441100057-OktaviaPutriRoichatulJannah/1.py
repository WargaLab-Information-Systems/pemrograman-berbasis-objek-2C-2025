class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print("==== BERJALAN ====")
        print(f"{self.nama} yang berusia {self.umur} tahun sedang bejalan menikmati pemandangan di kawasan {self.alamat}.")
        print()
    
    def berlari(self):
        print("==== BERLARI ====")
        print(f"{self.nama} yang berusia {self.umur} tahun sedang berlari cepat menuju rumahnya di kawasan {self.alamat}.")
        print()
    
human1 = Manusia("Adit",11,"Mulyoagung") 
human2 = Manusia("Ikhul",14,"Bakung")
human3 = Manusia("Zami",9,"Cungkup")
human4 = Manusia("Nabil",26, "Kebonsari")
human5 = Manusia("Lana",17, "Simo")  

human1.berlari()
human2.berjalan()
human3.berlari()
human4.berjalan()
human5.berlari()
