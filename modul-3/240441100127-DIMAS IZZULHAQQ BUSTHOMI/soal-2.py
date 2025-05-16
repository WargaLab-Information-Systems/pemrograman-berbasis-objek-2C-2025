class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan
    
    def estimasi_waktu(self):
        return 7

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        super().__init__(asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
    
    def estimasi_waktu(self):
        if self.jenis_kendaraan == "motor":
            return 2
        elif self.jenis_kendaraan == "truck":
            return 3
        else:
            return 0

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai  = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "garuda cargo":
            return 2
        elif self.maskapai == "batik air cargo":
            return 3
        else:
            return 0

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        waktu_darat = PengirimanDarat.estimasi_waktu(self)
        waktu_udara = PengirimanUdara.estimasi_waktu(self)

        estimasi_awal = Pengiriman.estimasi_waktu(self)

        if self.tujuan == "luar negeri":
            return waktu_darat + waktu_udara + 3, estimasi_awal + 3
        elif self.tujuan == "antar provinsi":
            return waktu_darat + waktu_udara + 1, estimasi_awal + 1
        elif self.tujuan == "antar kota":
            return waktu_darat, estimasi_awal
        
    
    def info(self,no):
        estimasi_faster, estimasi_longer = PengirimanInternasional.estimasi_waktu(self)
        print(f"{no}. Pengiriman asal     : {self.asal}")
        print(f"   Tujuan              : {self.tujuan}")
        print(f"   Jenis kendaraan     : {self.jenis_kendaraan} dan {self.maskapai}")
        print(f"   Estimasi Sampai     : {estimasi_faster} - {estimasi_longer} hari.")
        print("-----" * 8)

list_pengiriman = []

while True:
    print("-----" * 10)
    asal = input("Masukkan asal pengiriman : ")
    print("-----" * 8)
    print("Daftar Tujuan :\n 1. Luar Negeri\n 2. Antar Provinsi\n 3. Antar Kota")
    print("-----" * 8)

    tujuan = input("Pilih tujuan pengiriman : ")
    if tujuan == "1":
        tujuan = "luar negeri"

        print("-----" * 8)
        print("Daftar Maskapai :\n 1. Garuda Cargo\n 2. Batik Air Cargo")
        print("-----" * 8)
        maskapai = input("Pilih maskapai : ")
        if maskapai == "1":
            maskapai = "garuda cargo"
            print("-----" * 8)
            print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
            print("-----" * 8)
            jenis_kendaraan = input("Pilih jenis kendaraan : ")
            print("-----" * 8)
            if jenis_kendaraan == "1":
                jenis_kendaraan = "motor"
            elif jenis_kendaraan == "2":
                jenis_kendaraan = "truck"

            pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

        elif maskapai == "2":
            maskapai = "batik air cargo"
            print("-----" * 8)
            print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
            jenis_kendaraan = input("Pilih jenis kendaraan : ")
            print("-----" * 8)
            if jenis_kendaraan == "1":
                jenis_kendaraan = "motor"
            elif jenis_kendaraan == "2":
                jenis_kendaraan = "truck"
            
            pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

    elif tujuan == "2":
        tujuan = "antar provinsi"
        
        print("-----" * 8)
        kendaraan = input("Apakah Pengiriman menggunakan maskapai (y/n)? ")
        print("-----" * 8)
        if kendaraan == "y":
            print("Daftar Maskapai :\n 1. Garuda Cargo\n 2. Batik Air Cargo")
            print("-----" * 8)
            maskapai = input("Pilih maskapai : ")
            print("-----" * 8)
            if maskapai == "1":
                maskapai = "garuda cargo"
                print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
                print("-----" * 8)
                jenis_kendaraan = input("Pilih jenis kendaraan : ")
                print("-----" * 8)
                if jenis_kendaraan == "1":
                    jenis_kendaraan = "motor"
                elif jenis_kendaraan == "2":
                    jenis_kendaraan = "truck"

                pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

            elif maskapai == "2":
                maskapai = "batik air cargo"
                print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
                print("-----" * 8)
                jenis_kendaraan = input("Pilih jenis kendaraan : ")
                print("-----" * 8)
                if jenis_kendaraan == "1":
                    jenis_kendaraan = "motor"
                elif jenis_kendaraan == "2":
                    jenis_kendaraan = "truck"
                
                pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)
                
        elif kendaraan == "n":
            maskapai = "tidak menggunakan maskapai"
            print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
            print("-----" * 8)
            jenis_kendaraan = input("Pilih jenis kendaraan : ")
            print("-----" * 8)
            if jenis_kendaraan == "1":
                jenis_kendaraan = "motor"
            elif jenis_kendaraan == "2":
                jenis_kendaraan = "truck"

            pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

    elif tujuan == "3":
        tujuan = "antar kota"

        print("-----" * 8)
        print("Daftar Kendaraan Kurir :\n 1. Motor\n 2. Truck")
        print("-----" * 8)
        jenis_kendaraan = input("Pilih jenis kendaraan : ")
        print("-----" * 8)
        if jenis_kendaraan == "1":
            jenis_kendaraan = "motor"
        elif jenis_kendaraan == "2":
            jenis_kendaraan = "truck"

        maskapai = "tidak menggunakan maskapai"
        
        pengiriman = PengirimanInternasional(asal, tujuan, jenis_kendaraan, maskapai)

    list_pengiriman.append(pengiriman)

    print(f"Estimasi daratnya : {PengirimanDarat.estimasi_waktu(pengiriman)} hari.")
    print(f"Estimasi udaranya : {PengirimanUdara.estimasi_waktu(pengiriman)} hari.")
    if tujuan == "luar negeri":
        print("Estimasi tambahan ke luar negeri : 3 hari.")
    elif tujuan == "antar provinsi":
        print("Estimas tambahan antar provinsi : 1 hari.")
    estimasi_tercepat, estimasi_terlama = pengiriman.estimasi_waktu()
    print(f"Estimasi pengiriman barang {asal} ke {tujuan} : {estimasi_tercepat} - {estimasi_terlama} hari.")
    print("-----" * 8)

    cek = input("Apakah ingin mengirim lagi? (y/n) ")
    print("-----" * 8)
    if cek != "y":
        no = 1
        print("Data Pengiriman : ")
        for data in list_pengiriman:
            data.info(no)

            no += 1
        break
        
