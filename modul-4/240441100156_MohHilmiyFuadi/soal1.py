class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo_awal, pin):
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal
        self.__pin = pin 

    def get_no_rekening(self):
        return self.__no_rekening

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def verifikasi_pin(self, pin):
        return self.__pin == pin

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print("Setoran berhasil.")
        else:
            print("Jumlah tidak valid.")

    def tarik(self, jumlah, pin):
        if not self.verifikasi_pin(pin):
            print("PIN salah.")
            return

        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print("Penarikan berhasil.")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid.")

    def tampilkan_info(self):
        print(f"No Rekening : {self.get_no_rekening()}")
        print(f"Nama Pemilik: {self.get_nama_pemilik()}")
        print(f"Saldo       : {self.get_saldo()}")
        print("---------------------------")


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)
        print("Rekening berhasil ditambahkan.")

    def cari_rekening(self, no_rekening):
        for rek in self.rekening_list:
            if rek.get_no_rekening() == no_rekening:
                return rek
        return None

    def setor(self, no_rekening, jumlah):
        rek = self.cari_rekening(no_rekening)
        if rek:
            rek.setor(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tarik(self, no_rekening, jumlah, pin):
        rek = self.cari_rekening(no_rekening)
        if rek:
            rek.tarik(jumlah, pin)
        else:
            print("Rekening tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Belum ada rekening.")
        else:
            for rek in self.rekening_list:
                rek.tampilkan_info()


def main():
    bank = Bank()

    while True:
        print("\n=== MENU BANK ===")
        print("1. Tambah Rekening")
        print("2. Setor")
        print("3. Tarik")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            no_rek = input("No Rekening   : ")
            nama = input("Nama Pemilik  : ")
            saldo = float(input("Saldo Awal    : "))
            pin = input("PIN (4 digit) : ")
            rekening = RekeningBank(no_rek, nama, saldo, pin)
            bank.tambah_rekening(rekening)

        elif pilihan == '2':
            no_rek = input("No Rekening   : ")
            jumlah = float(input("Jumlah Setor  : "))
            bank.setor(no_rek, jumlah)

        elif pilihan == '3':
            no_rek = input("No Rekening   : ")
            jumlah = float(input("Jumlah Tarik  : "))
            pin = input("Masukkan PIN  : ")
            bank.tarik(no_rek, jumlah, pin)

        elif pilihan == '4':
            bank.tampilkan_semua_rekening()

        elif pilihan == '5':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
    # di menu tarik tambahkan pin