class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    @property
    def no_rek(self): #getter untuk no_rek
        return self.__no_rek

    @property 
    def nama_pemilik(self): #getter untuk nama_pemilik
        return self.__nama_pemilik

    @nama_pemilik.setter
    def nama_pemilik(self, nama_baru): #setter untuk nama_pemilik
        self.__nama_pemilik = nama_baru

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def tampil(self):
        print(f"No Rekening  : {self.__no_rek}")
        print(f"Nama Pemilik : {self.__nama_pemilik}")
        print(f"Saldo        : {self.__saldo}")
        print("-" * 30)


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)

    def cari_rekening(self, no_rek):
        for rek in self.rekening_list:
            if rek.no_rek == no_rek:
                return rek
        return None

    def setor_uang(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.setor(jumlah)
            print("Setoran berhasil.")
        else:
            print("Rekening tidak ditemukan.")

    def tarik_uang(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            if rek.tarik(jumlah):
                print("Penarikan berhasil.")
            else:
                print("Saldo tidak cukup.")
        else:
            print("Rekening tidak ditemukan.")

    def tampil_semua_rekening(self):
        if not self.rekening_list:
            print("Belum ada data rekening.")
        else:
            for rek in self.rekening_list:
                rek.tampil()


# MAIN PROGRAM
def main():
    bank = Bank()
    while True:
        print("\nMenu:")
        print("1. Tambah Rekening")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            no_rek = input("Masukkan No Rekening: ")
            nama = input("Masukkan Nama Pemilik: ")
            saldo = float(input("Masukkan Saldo Awal: "))
            rek = RekeningBank(no_rek, nama, saldo)
            bank.tambah_rekening(rek)
            print("Rekening berhasil ditambahkan.")

        elif pilihan == "2":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan jumlah setoran: "))
            bank.setor_uang(no_rek, jumlah)

        elif pilihan == "3":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan jumlah penarikan: "))
            bank.tarik_uang(no_rek, jumlah)

        elif pilihan == "4":
            bank.tampil_semua_rekening()

        elif pilihan == "5":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()