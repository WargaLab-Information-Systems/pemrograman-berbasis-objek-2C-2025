class RekeningBank:
    def __init__(self, no_rek, nama, saldo):
        self.__no_rek = no_rek
        self.__nama = nama
        self.__saldo = saldo
    
    @property
    def no_rek(self):
        return self.__no_rek
    
    @property
    def nama(self):
        return self.__nama
    
    @property
    def saldo(self):
        return self.__saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran sebesar Rp{jumlah:,} berhasil.")
        else:
            print("Jumlah setoran tidak valid")
    
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan sebesar Rp{jumlah:,} berhasil.")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid")

    def info(self):
        print(f"No Rek: {self.__no_rek} | Nama: {self.__nama} | Saldo: Rp{self.__saldo:,}")


class Bank:
    def __init__(self):
        self.daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.daftar_rekening.append(rekening)
        print("Rekening berhasil ditambahkan.")

    def cari_rekening(self, no_rek):
        for r in self.daftar_rekening:
            if r.no_rek == no_rek:
                return r
        return None

    def setor(self, no_rek, jumlah):
        r = self.cari_rekening(no_rek)
        if r:
            r.setor(jumlah)
        else:
            print("Rekening tidak ditemukan!")

    def tarik(self, no_rek, jumlah):
        r = self.cari_rekening(no_rek)
        if r:
            r.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan!")

    def tampilkan_semua(self):
        if not self.daftar_rekening:
            print("Belum ada rekening.")
        else:
            print("\n===== Data Semua Rekening =====")
            for r in self.daftar_rekening:
                r.info()


def is_angka_valid(nilai):
    return nilai.isdigit()


def main():
    bank = Bank()
    
    while True:
        print("\n===== MENU BANK =====")
        print("1. Tambah Rekening")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            no_rek = input("Masukkan No Rekening: ")
            nama = input("Masukkan Nama: ")
            saldo_input = input("Masukkan Saldo Awal: ")
            if is_angka_valid(saldo_input):
                saldo = float(saldo_input)
                rekening = RekeningBank(no_rek, nama, saldo)
                bank.tambah_rekening(rekening)
            else:
                print("Saldo harus berupa angka positif.")

        elif pilihan == "2":
            no_rek = input("Masukkan No Rekening: ")
            jumlah_input = input("Masukkan jumlah setoran: ")
            if is_angka_valid(jumlah_input):
                jumlah = float(jumlah_input)
                bank.setor(no_rek, jumlah)
            else:
                print("Jumlah harus berupa angka positif.")

        elif pilihan == "3":
            no_rek = input("Masukkan No Rekening: ")
            jumlah_input = input("Masukkan jumlah penarikan: ")
            if is_angka_valid(jumlah_input):
                jumlah = float(jumlah_input)
                bank.tarik(no_rek, jumlah)
            else:
                print("Jumlah harus berupa angka positif.")

        elif pilihan == "4":
            bank.tampilkan_semua()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan layanan bank.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()