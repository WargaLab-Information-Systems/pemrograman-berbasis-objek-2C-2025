class manusia:
    def __init__(self, nama, umur, alamat, aktivitas):
        self.nama=nama
        self.umur=umur
        self.alamat=alamat
        self.aktivitas=aktivitas

    def display (self):
        print("=========DATA MANUSIA=========")
        print("Nama     :",self.nama)
        print("Umur     :",self.umur)
        print("alamat   :",self.alamat)
        print("Aktivitas: ", self.aktivitas)
        print("=" * 30)

  
manusia1=manusia("Sahrul", 19, "Jl.Banjarsari", "Data di atas sedang berlari")
manusia2=manusia("Sely", 20, "Jl.Brangkal", "Data di atas sedang berjalan")
manusia3=manusia("Amin", 18, "Jl.Kenjeran", "Data di atas sedang berjalan")
manusia4=manusia("Alif", 21, "Jl.Sudirman", "Data di atas sedang berjalan")
manusia5=manusia("Faisal", 22, "Jl.Trunojoyo", "Data di atas sedang berjalan")

manusia1.display()
manusia2.display()
manusia3.display()
manusia4.display()
manusia5.display()