class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo):
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    @property
    def no_rekening(self):
        return self.__no_rekening

    @property
    def nama_pemilik(self):
        return self.__nama_pemilik

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah):
        if jumlah >= 0:
            self.__saldo = jumlah
        else:
            print("Saldo tidak boleh negatif!")

    def setor_saldo(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setoran sebesar {jumlah} berhasil.")
        else:
            print("Jumlah setoran harus lebih dari 0.")

    def tarik_saldo(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Penarikan sebesar {jumlah} berhasil.")
        else:
            print("Saldo tidak mencukupi atau jumlah tidak valid.")

    def tampilkan_info(self):
        print(f"No Rekening: {self.no_rekening}, Nama: {self.nama_pemilik}, Saldo: {self.saldo}")

class Bank:
    def __init__(self):
        self.rekening_list = []

    def cari_rekening(self, no_rekening):
        for rekening in self.rekening_list:
            if rekening.no_rekening == no_rekening:
                return rekening
        return None

    def tambah_rekening(self, rekening):
        if self.cari_rekening(rekening.no_rekening):
            print("Nomor rekening sudah terdaftar.")
        else:
            self.rekening_list.append(rekening)
            print(f"Rekening atas nama {rekening.nama_pemilik} berhasil ditambahkan.")

    def hapus_rekening(self, no_rekening):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            self.rekening_list.remove(rekening)
            print("Rekening berhasil dihapus.")
        else:
            print("Rekening tidak ditemukan.")

    def setor_saldo(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            rekening.setor_saldo(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tarik_saldo(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            rekening.tarik_saldo(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Belum ada rekening.")
        else:
            print("\nData Rekening:")
            for rekening in self.rekening_list:
                rekening.tampilkan_info()

def menu():
    bank = Bank()

    while True:
        print("\n===== MENU BANK =====")
        print("1. Tambah Rekening")
        print("2. Setor Saldo")
        print("3. Tarik Saldo")
        print("4. Hapus Rekening")
        print("5. Tampilkan Semua Rekening")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            no_rek = input("Masukkan No Rekening: ")
            nama = input("Masukkan Nama Pemilik: ")
            saldo = float(input("Masukkan Saldo Awal: "))
            bank.tambah_rekening(RekeningBank(no_rek, nama, saldo))

        elif pilihan == "2":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan Jumlah Setoran: "))
            bank.setor_saldo(no_rek, jumlah)

        elif pilihan == "3":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = float(input("Masukkan Jumlah Penarikan: "))
            bank.tarik_saldo(no_rek, jumlah)

        elif pilihan == "4":
            no_rek = input("Masukkan No Rekening yang ingin dihapus: ")
            bank.hapus_rekening(no_rek)

        elif pilihan == "5":
            bank.tampilkan_semua_rekening()

        elif pilihan == "6":
            print("Terima kasih telah menggunakan layanan kami.")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
