class kucing:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Kucing ===")
        print(f"Warna : {self.warna}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"Pemilik : {self.pemilik}")
        print(" ")

class hamster:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Hamster ===")
        print(f"Warna : {self.warna}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"Pemilik : {self.pemilik}")
        print(" ")        

class kelinci:
    def __init__(self, warna, jenis_kelamin, pemilik):
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        self.pemilik = pemilik

    def tampilkan_hewan(self):
        print("=== Kelinci ===")
        print(f"Warna : {self.warna}")
        print(f"Jenis Kelamin : {self.jenis_kelamin}")
        print(f"Pemilik : {self.pemilik}")
        print(" ")  


while True :
    jenis_hewan = input("Masukkan Hewan (Kucing/Hamster/Kelinci) atau 'selesai' untuk berhenti: ").lower()

    if jenis_hewan == "selesai":
        break
    if jenis_hewan not in ["kucing","hamster","kelinci"] :
        print("Jenis Hewan Tidak Valid Silahkan Masukkan Kucing, Hamster, atau Kelinci.")

    warna = input("Masukkan Warna : ")
    jenis_kelamin = input("Masukkan Jenis Kelamin : ")
    pemilik = input("Masukkan Pemilik : ")

    if jenis_hewan == "kucing":
        kucing = kucing(warna, jenis_kelamin, pemilik)
        kucing.tampilkan_hewan()

    elif jenis_hewan == "hamster":
        hamster = hamster(warna, jenis_kelamin, pemilik)
        hamster.tampilkan_hewan()

    elif jenis_hewan == "kelinci":
        kelinci = kelinci(warna, jenis_kelamin, pemilik)
        kelinci.tampilkan_hewan()    

