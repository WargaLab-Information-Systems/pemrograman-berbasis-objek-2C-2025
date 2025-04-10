class mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def display(self):
        print("Namanya adalah :", self.nama)
        print("NIM adalah :", self.nim)
        print("IPKnya adalah :", self.ipk)

mhs = mahasiswa("Alip", "24130", 4.0)
mhs.display()