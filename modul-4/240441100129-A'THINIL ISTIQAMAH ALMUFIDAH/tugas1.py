class RekeningBank:
    def __init__(self, no_rek, nama, saldo=0, pin="0000"):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo
        self.__pin = pin

    @property
    def no_rek(self):
        return self.__no_rek

    @property
    def nama(self):
        return self.__nama

    @property
    def saldo(self):
        return self.__saldo

    @property
    def info(self):
        return f"No Rek: {self.__no_rek}, Nama: {self.__nama}, Saldo: {self.__saldo}"

    def verifikasi_pin(self, input_pin):
        return self.__pin == input_pin

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran berhasil: +{jumlah}")
            print(f"Saldo setelah setoran: {self.__saldo}")
        else:
            print("Jumlah setoran harus lebih dari 0.")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup untuk penarikan.")
        elif jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0.")
        else:
            self.__saldo -= jumlah
            print(f"Penarikan berhasil: -{jumlah}")
            print(f"Saldo setelah penarikan: {self.__saldo}")


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, no_rek, nama, saldo_awal=0, pin="0000"):
        for rekening in self.rekening_list:
            if rekening.no_rek == no_rek:
                print("Nomor rekening sudah terdaftar.")
                return
        rekening_baru = RekeningBank(no_rek, nama, saldo_awal, pin)
        self.rekening_list.append(rekening_baru)
        print("Rekening berhasil ditambahkan.")
        print(f"Nomor Rekening: {no_rek}")
        print(f"PIN           : {pin}")

    def cari_rekening(self, no_rek):
        for rekening in self.rekening_list:
            if rekening.no_rek == no_rek:
                return rekening
        print("Rekening tidak ditemukan.")
        return None

    def setor_uang(self, no_rek, jumlah, pin):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            if rekening.verifikasi_pin(pin):
                rekening.setor(jumlah)
            else:
                print("PIN salah.")

    def tarik_uang(self, no_rek, jumlah, pin):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            if rekening.verifikasi_pin(pin):
                rekening.tarik(jumlah)
            else:
                print("PIN salah.")

    def tampilkan_semua_rekening(self):
        if not self.rekening_list:
            print("Belum ada rekening terdaftar.")
        else:
            print("Data semua rekening:")
            for rekening in self.rekening_list:
                print(rekening.info)


def main():
    print("--- PILIH BANK ---")
    print("1. BCA")
    print("2. BRI")
    print("3. Mandiri")
    print("4. BNI")
    pilihan_bank = input("Pilih bank (1-4): ")

    if pilihan_bank == '1':
        nama_bank = "BCA"
    elif pilihan_bank == '2':
        nama_bank = "BRI"
    elif pilihan_bank == '3':
        nama_bank = "Mandiri"
    elif pilihan_bank == '4':
        nama_bank = "BNI"
    else:
        print("Pilihan tidak valid. Program dihentikan.")
        return

    print(f"\nBank yang dipilih: {nama_bank}")
    bank = Bank()

    while True:
        print("\n--- MENU BANK ---")
        print("1. Tambah Rekening")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            no_rek = input("Masukkan nomor rekening: ")
            nama = input("Masukkan nama pemilik: ")
            try:
                saldo = int(input("Masukkan saldo awal: "))
            except ValueError:
                print("Input tidak valid. Saldo harus berupa angka.")
                continue
            pin = input("Masukkan PIN (4 digit): ")
            bank.tambah_rekening(no_rek, nama, saldo, pin)

        elif pilihan == '2':
            no_rek = input("Masukkan nomor rekening: ")
            pin = input("Masukkan PIN: ")
            try:
                jumlah = int(input("Masukkan jumlah setoran: "))
            except ValueError:
                print("Input tidak valid. Jumlah setoran harus berupa angka.")
                continue
            bank.setor_uang(no_rek, jumlah, pin)

        elif pilihan == '3':
            no_rek = input("Masukkan nomor rekening: ")
            pin = input("Masukkan PIN: ")
            try:
                jumlah = int(input("Masukkan jumlah penarikan: "))
            except ValueError:
                print("Input tidak valid. Jumlah penarikan harus berupa angka.")
                continue
            bank.tarik_uang(no_rek, jumlah, pin)

        elif pilihan == '4':
            bank.tampilkan_semua_rekening()

        elif pilihan == '5':
            print("Terima kasih telah menggunakan layanan bank.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
# pin bank sama hasil setor dan tarik


