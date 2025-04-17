class manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat= alamat

    def berjalan(self):
        return f"Si {self.nama} sedang berjalan bersama orangtua nya."

    def berlari(self):
        return f"Si {self.nama} sedang berlari bersama teman-temannya."

jefri = manusia("jefri", 18, "Sumenep")
sekar = manusia("sekar", 19, "Pamekasan")
bassam = manusia("bassam", 22, "Surabaya")
dewi = manusia("dewi", 24, "Yogyakarta")
raden = manusia("raden", 27, "Medan")

print(jefri.berjalan())
print(sekar.berlari())
print(bassam.berjalan())
print(dewi.berlari())
print(raden.berjalan())