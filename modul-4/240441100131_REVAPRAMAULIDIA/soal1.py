#setor saldonya nambah dari saldo awal,tarik mengurang saldo berdasarkan rekening ,hapus rekening,kalau saldo ada gabisa dihps
class RekeningBank:
    def __init__(self, nomor_rekening, nama, saldo):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo

    def set_setoran(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setoran harus lebih dari 0")

    def set_penarikan(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True  
        else:
            print("Saldo anda kurang atau penarikan tidak valid.")
            return False  

    def get_info(self):
        print(f"Nama   : {self.nama}")
        print(f"No Rek : {self.nomor_rekening}")
        print(f"Saldo  : Rp {self.__saldo}")

    def get_no_rek(self):
        return self.nomor_rekening

    def get_saldo(self):
        return self.__saldo


class Bank:
    def __init__(self):
        self.data_rekening = []

    def tambah_rekening(self, rekening):
        if self.cari_rekening(rekening.get_no_rek()) is None:
            self.data_rekening.append(rekening)
        else:
            print("Nomor rekening sudah ada, tidak bisa ditambahkan.")

    def cari_rekening(self, no_rek):
        for i in self.data_rekening:
            if i.get_no_rek() == no_rek:
                return i
        return None

    def tarik(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            berhasil = rek.set_penarikan(jumlah)
            if berhasil:
                print("Penarikan berhasil")
        else:
            print("Rekening tidak ditemukan")

    def setor(self, no_rek, jumlah):
        rek = self.cari_rekening(no_rek)
        if rek:
            rek.set_setoran(jumlah)
            print("Setoran berhasil")
        else:
            print("Rekening tidak ditemukan")

    def info_rekening(self):
        if not self.data_rekening:
            print("Tidak ada rekening")
        else:
            for i in self.data_rekening:
                i.get_info()

    def hapus_rekening(self, no_rek):
        rek = self.cari_rekening(no_rek)
        if rek:
            saldo = rek.get_saldo()
            if saldo == 0:
                self.data_rekening.remove(rek)
                print(f"Rekening {no_rek} berhasil dihapus.")
            else:
                print("Saldo rekening tidak nol, tidak bisa dihapus.")
        else:
            print("Rekening tidak ditemukan.")


def buat_rekening():
    nama = input("Nama: ").strip()
    while True:
        no_rek = input("No Rek (16 digit): ").strip()
        if no_rek.isdigit() and len(no_rek) == 16:
            break
        else:
            print("Nomor rekening harus berupa 16 digit angka.")
    while True:
        saldo = input("Saldo awal: ").strip()
        try:
            saldo = float(saldo)
            if saldo >= 0:
                break
            else:
                print("Saldo tidak boleh negatif.")
        except ValueError:
            print("Saldo harus berupa angka.")
    return RekeningBank(no_rek, nama, saldo)


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nMenu:")
        print("1. Tambah rekening")
        print("2. Setor")
        print("3. Tarik")
        print("4. Lihat info rekening tertentu")
        print("5. Info semua rekening")
        print("6. Hapus rekening")
        print("7. Keluar")

        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ")

        if pilihan == "1":
            rekening_baru = buat_rekening()
            bank.tambah_rekening(rekening_baru)
            print("Rekening baru berhasil ditambahkan.")

        elif pilihan == "2":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = input("Jumlah setoran: ")
            try:
                rek = bank.cari_rekening(no_rek)
                if rek:
                    saldo_awal = rek.get_saldo()
                    print(f"Saldo awal: Rp {saldo_awal}")
                    jumlah_setor = float(jumlah)
                    print(f"Jumlah setoran: Rp {jumlah_setor}")
                    bank.setor(no_rek, jumlah_setor)
                    saldo_baru = rek.get_saldo()
                    print(f"Saldo setelah setoran: Rp {saldo_baru}")
                else:
                    print("Rekening tidak ditemukan.")
            except ValueError:
                print("Jumlah harus berupa angka.")

        elif pilihan == "3":
            no_rek = input("Masukkan No Rekening: ")
            jumlah = input("Jumlah penarikan: ")
            try:
                rek = bank.cari_rekening(no_rek)
                if rek:
                    saldo_awal = rek.get_saldo()
                    print(f"Saldo awal: Rp {saldo_awal}")
                    jumlah_tarik = float(jumlah)
                    print(f"Jumlah penarikan: Rp {jumlah_tarik}")
                    berhasil = rek.set_penarikan(jumlah_tarik)
                    if berhasil:
                        print("Penarikan berhasil")
                        saldo_baru = rek.get_saldo()
                        print(f"Saldo setelah penarikan: Rp {saldo_baru}")
                    else:
                        print("Penarikan gagal, saldo tidak cukup atau penarikan tidak valid.")
                else:
                    print("Rekening tidak ditemukan.")
            except ValueError:
                print("Jumlah harus berupa angka.")

        elif pilihan == "4":
            no_rek = input("Masukkan No Rekening: ")
            rek = bank.cari_rekening(no_rek)
            if rek:
                rek.get_info()
            else:
                print("Rekening tidak ditemukan.")

        elif pilihan == "5":
            print("=== Info Semua Rekening ===")
            bank.info_rekening()

        elif pilihan == "6":
            no_rek = input("Masukkan No Rekening yang ingin dihapus: ")
            bank.hapus_rekening(no_rek)

        elif pilihan == "7":
            print("Terima kasih telah menggunakan layanan kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1/2/3/4/5/6/7")