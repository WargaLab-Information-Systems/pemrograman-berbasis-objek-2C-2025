class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print( f"{self.nama} yang berumur {self.umur} tahun dan tinggal di {self.alamat} kini dapat berjalan.")
    
    def berlari(self):
        return f"{self.nama} yang berumur {self.umur} tahun dan tinggal di {self.alamat} kini dapat berlari dengan kencang."
    
mns1 = manusia("Adit", 3, "Jl. Mawar")
mns2 = manusia("Salsa", 6, "Jl. Melati")
mns3 = manusia("Aurel", 12, "Jl. Bola")
mns4 = manusia("Aiz", 8, "Jl. Pahlawan")
mns5 = manusia("Puput", 4, "Jl. Jayanegara")

# print(f"1. {mns1.berjalan()}")
# print(f"2. {mns2.berlari()}")
# print(f"3. {mns3.berjalan()}")
# print(f"4. {mns4.berlari()}")
# print(f"5. {mns5.berjalan()}")
mns1.berjalan()