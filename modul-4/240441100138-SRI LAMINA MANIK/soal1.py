class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama = nama_pemilik
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_saldo(self, saldo_baru):
        self.__saldo = saldo_baru

    def get_info(self):
        return f"No.Rek: {self.__no_rek}, Nama: {self.__nama}, Saldo: Rp{self.__saldo}"

    def setor(self, jumlah):
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo kamu tidak cukup.")


class Bank:
    def __init__(self):
        self.rekening = []

    def tambah_rekening(self, rek):
        self.rekening.append(rek)

    def cari_rekening_by_no(self, no_rek):
        for r in self.rekening:
            if r.get_no_rek() == no_rek:
                return r
        return None

    def cari_rekening_by_nama(self, nama):
        for r in self.rekening:
            if r.get_nama().lower() == nama.lower():
                return r
        return None

    def setor_uang(self, no_rek, jumlah):
        rek = self.cari_rekening_by_no(no_rek)
        if rek:
            rek.setor(jumlah)
            print("Setor berhasil.")
        else:
            print("Rekening tidak ditemukan.")

    def tarik_uang(self, no_rek, jumlah):
        rek = self.cari_rekening_by_no(no_rek)
        if rek:
            rek.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def menampilkan_semua_rekening(self):
        print("\nDaftar Semua Rekening:")
        for r in self.rekening:
            print(r.get_info())

    def update_rekening_by_nama(self, nama):
        rek = self.cari_rekening_by_nama(nama)
        if rek:
            print("Rekening ditemukan:")
            print(rek.get_info())
            new_nama = input("Masukkan nama baru (tekan Enter jika tidak ingin mengganti): ")
            if new_nama.strip():
                rek.set_nama(new_nama)
                print("Data berhasil diupdate.")
        else:
            print("Nama tidak ditemukan.")

    def hapus_rekening(self):
        if not self.rekening:
            print("Tidak ada rekening yang bisa dihapus.")
            return

        self.menampilkan_semua_rekening()
        no_rek = input("Masukkan No. Rekening yang ingin dihapus: ")
        rek = self.cari_rekening_by_no(no_rek)

        if rek:
            self.rekening.remove(rek)
            print(f"Rekening '{rek.get_no_rek()}' atas nama '{rek.get_nama()}' berhasil dihapus.")
        else:
            print("Rekening tidak ditemukan.")


# Program utama
bank = Bank()

jumlah_rek = int(input("Berapa rekening yang ingin didaftarkan?: "))
for i in range(jumlah_rek):
    print(f"\nInput Rekening ke-{i+1}")
    no = input("Masukkan No. Rekening: ")
    nama = input("Masukkan Nama Pemilik: ")
    saldo = int(input("Masukkan Saldo Awal: "))
    bank.tambah_rekening(RekeningBank(no, nama, saldo))

while True:
    print("\nMENU BANK")
    print("1. Setor Uang")
    print("2. Tarik Uang")
    print("3. Lihat Semua Rekening")
    print("4. Update Rekening (berdasarkan nama)")
    print("5. Hapus Rekening")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        no = input("Masukkan No. Rekening: ")
        jumlah = int(input("Masukkan jumlah yang disetor: "))
        bank.setor_uang(no, jumlah)
    elif pilihan == "2":
        no = input("Masukkan No. Rekening: ")
        jumlah = int(input("Masukkan jumlah yang ditarik: "))
        bank.tarik_uang(no, jumlah)
    elif pilihan == "3":
        bank.menampilkan_semua_rekening()
    elif pilihan == "4":
        nama = input("Masukkan nama pemilik rekening yang ingin diupdate: ")
        bank.update_rekening_by_nama(nama)
    elif pilihan == "5":
        bank.hapus_rekening()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan layanan bank.")
        break
    else:
        print("Pilihan tidak valid.")
