class data:
    # model
    def __init__(self, nama, nim, tahun_lahir, gender, status): # construktor
        # inisialisasi attributes
        self.nama = nama
        self.nim = nim
        self.tahun_lahir = tahun_lahir
        self.gender = gender
        self.status = status
    
    # control
    def perkenalkan(self):
        print(f"Saya ", self.nama, "NIM ", self.nim, self.tahun_lahir, "line,", self.gender, "dan berstatus", self.status)

# visual
data1 = data("Niha", "240441100006", "2006", "female", "taken") # object yang ada di dalam class data
data2 = data("Zayne", "24044110000", "1996", "male", "taken")

# pemanggilan method
data1.perkenalkan()
data2.perkenalkan()