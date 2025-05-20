class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo_awal):
        self.__no_rekening = no_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal
    def get_no_rekening(self):
        return self.__no_rekening
    def set_no_rekening(self, no_rekening):
        self.__no_rekening = no_rekening
    def get_nama_pemilik(self):
        return self.__nama_pemilik
    def set_nama_pemilik(self, nama_pemilik):
        self.__nama_pemilik = nama_pemilik
    def get_saldo(self):
        return self.__saldo
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus lebih besar dari 0.")
    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        else:
            print("Saldo tidak cukup untuk penarikan.")
            return False
    def tampilkan_info(self):
        print(f"No Rekening : {self.__no_rekening}")
        print(f"Nama Pemilik: {self.__nama_pemilik}")
        print(f"Saldo       : {self.__saldo}")
        print("-" * 30)
class Bank:
    def __init__(self):
        self.daftar_rekening = []
    def tambah_rekening(self, no_rek, nama, saldo_awal):
        if self.cari_rekening(no_rek):
            print("No rekening sudah terdaftar.")
            return
        rekening = RekeningBank(no_rek, nama, saldo_awal)
        self.daftar_rekening.append(rekening)
        print("Rekening berhasil ditambahkan.")
    def setor_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            rekening.setor(jumlah)
            print("Setoran berhasil.")
        else:
            print("Rekening tidak ditemukan.")
    def tarik_uang(self, no_rek, jumlah):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            if rekening.tarik(jumlah):
                print("Penarikan berhasil.")
            else:
                print("Penarikan gagal.")
        else:
            print("Rekening tidak ditemukan.")
    def cari_rekening(self, no_rek):
        for rek in self.daftar_rekening:
            if rek.get_no_rekening() == no_rek:
                return rek
        return None
    def tampilkan_semua_rekening(self):
        if not self.daftar_rekening:
            print("Belum ada rekening yang terdaftar.")
        else:
            print("\n=== Data Semua Rekening ===")
            for rek in self.daftar_rekening:
                rek.tampilkan_info()
    def hapus_rekening(self, no_rek):
        rekening = self.cari_rekening(no_rek)
        if rekening:
            self.daftar_rekening.remove(rekening)
            print("Rekening berhasil dihapus.")
        else:
            print("Rekening tidak ditemukan.")
    def edit_rekening(self, no_lama):
        rekening = self.cari_rekening(no_lama)
        if not rekening:
            print("Rekening tidak ditemukan.")
            return
        no_baru = input("Masukkan No Rekening baru: ")
        while not self.validasi_input_nomor(no_baru) or (no_baru != no_lama and self.cari_rekening(no_baru)):
            print("❌ No rekening tidak valid atau sudah terdaftar.")
            no_baru = input("Masukkan No Rekening baru: ")
        nama_baru = input("Masukkan Nama Pemilik baru: ")
        while not self.validasi_input_nama(nama_baru) or any(rek.get_nama_pemilik() == nama_baru and rek != rekening for rek in self.daftar_rekening):
            print("❌ Nama pemilik tidak valid atau sudah digunakan.")
            nama_baru = input("Masukkan Nama Pemilik baru: ")
        rekening.set_no_rekening(no_baru)
        rekening.set_nama_pemilik(nama_baru)
        print("✅ Data rekening berhasil diperbarui.")
    def validasi_input_nomor(self, input_string):
        return input_string.isdigit()
    def validasi_input_nama(self, input_string):
        return input_string.isalpha()

bank = Bank()
while True:
    print("\n=== MENU BANK ===")
    print("1. Tambah Rekening")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Tampilkan Semua Rekening/Hapus")
    print("5. Edit Rekening")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        no = input("Masukkan No Rekening: ")
        while not bank.validasi_input_nomor(no):
            print("No rekening harus berupa angka.")
            no = input("Masukkan No Rekening: ")
        nama = input("Masukkan Nama Pemilik: ")
        while not bank.validasi_input_nama(nama):
            print("Nama pemilik hanya boleh huruf.")
            nama = input("Masukkan Nama Pemilik: ")
        saldo = input("Masukkan Saldo Awal: ")
        while not saldo.isdigit():
            print("Saldo harus berupa angka.")
            saldo = input("Masukkan Saldo Awal: ")
        bank.tambah_rekening(no, nama, int(saldo))

    elif pilihan == "2":
        while True:
            no = input("Masukkan No Rekening: ")
            while not bank.validasi_input_nomor(no):
                print("No rekening harus berupa angka.")
                no = input("Masukkan No Rekening: ")
            rekening = bank.cari_rekening(no)
            if rekening:
                break
            else:
                print("❌ Rekening tidak ditemukan. Silakan coba lagi.")
        jumlah = input("Masukkan Jumlah Setoran: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah setoran harus angka positif.")
            jumlah = input("Masukkan Jumlah Setoran: ")
        rekening.setor(int(jumlah))
        print("Setoran berhasil.")
    elif pilihan == "3":
        while True:
            no = input("Masukkan No Rekening: ")
            while not bank.validasi_input_nomor(no):
                print("No rekening harus berupa angka.")
                no = input("Masukkan No Rekening: ")

            rekening = bank.cari_rekening(no)
            if rekening:
                break
            else:
                print("❌ Rekening tidak ditemukan. Silakan coba lagi.")
        jumlah = input("Masukkan Jumlah Penarikan: ")
        while not jumlah.isdigit() or int(jumlah) <= 0:
            print("Jumlah penarikan harus angka positif.")
            jumlah = input("Masukkan Jumlah Penarikan: ")
        if rekening.tarik(int(jumlah)):
            print("Penarikan berhasil.")
        else:
            print("Penarikan gagal.")
    elif pilihan == "4":
        if not bank.daftar_rekening:
            print("Belum ada rekening yang terdaftar.")
        else:
            bank.tampilkan_semua_rekening()
            sub = input("Apakah Anda ingin menghapus rekening? (y/n): ")
            if sub.lower() == 'y':
                while True:
                    no = input("Masukkan No Rekening yang ingin dihapus: ")
                    if not bank.validasi_input_nomor(no):
                        print("No rekening harus berupa angka.")
                        continue
                    if bank.cari_rekening(no):
                        bank.hapus_rekening(no)
                        break
                    else:
                        print("❌ Rekening tidak ditemukan. Silakan coba lagi.")
    elif pilihan == "5":
        while True:
            no = input("Masukkan No Rekening yang ingin diedit: ")
            if not bank.validasi_input_nomor(no):
                print("No rekening harus berupa angka.")
                continue
            if bank.cari_rekening(no):
                bank.edit_rekening(no)
                break
            else:
                print("❌ Rekening tidak ditemukan. Silakan coba lagi.")
    elif pilihan == "6":
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

#    tambahkan fitur edit pada nomor dan nama pemilik gaboleh sama kaya sebelumnya, delete rekening ditaruh di menu nomor 4, jadi total menu ada 6