class RekeningBank:
    def __init__(self, no_rekening, nama_pemilik, saldo_awal=0):
        self._nama_pemilik = nama_pemilik
        self.__no_rekening = no_rekening
        self.__saldo = saldo_awal

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai_baru):
        if isinstance(nilai_baru, (int, float)) and nilai_baru >= 0:
            self.__saldo = nilai_baru
            print("Saldo berhasil diubah.")
        else:
            print("Saldo tidak valid. Harus berupa angka dan tidak negatif.")

    @property
    def nama_pemilik(self):
        return self._nama_pemilik

    @nama_pemilik.setter
    def nama_pemilik(self, nama_baru):
        if isinstance(nama_baru, str) and nama_baru.strip():
            self._nama_pemilik = nama_baru
            print("Nama pemilik berhasil diubah.")
        else:
            print("Nama pemilik tidak valid.")

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran sebesar {jumlah} berhasil.")
        else:
            print("Jumlah setoran harus lebih dari 0.")

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        elif jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0.")
        else:
            self.__saldo -= jumlah
            print(f"Penarikan sebesar {jumlah} berhasil.")

    def get_info(self):
        return {
            "No Rekening": self.__no_rekening,
            "Nama Pemilik": self._nama_pemilik,
            "Saldo": self.__saldo
        }


class Bank:
    def __init__(self):
        self.daftar_rekening = []

    def tambah_rekening(self, rekening):
        self.daftar_rekening.append(rekening)
        print(f"Rekening atas nama {rekening.nama_pemilik} berhasil ditambahkan.")

    def cari_rekening(self, no_rekening):
        for rekening in self.daftar_rekening:
            if rekening.get_info()["No Rekening"] == no_rekening:
                return rekening
        return None

    def setor(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            rekening.setor(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tarik(self, no_rekening, jumlah):
        rekening = self.cari_rekening(no_rekening)
        if rekening:
            rekening.tarik(jumlah)
        else:
            print("Rekening tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        print("\nDaftar Rekening Nasabah:")
        for rekening in self.daftar_rekening:
            info = rekening.get_info()
            print(f"No Rekening: {info['No Rekening']}, Nama: {info['Nama Pemilik']}, Saldo: {info['Saldo']}")

bank = Bank()

rek1 = RekeningBank("001", "Andi", 1_000_000)
rek1.saldo =2000000
bank.tambah_rekening(rek1)
rek2 = RekeningBank("002", "Budi", 500_000)
rek2.nama_pemilik = ("Laila")
bank.tambah_rekening(rek2)
bank.tambah_rekening(RekeningBank("003", "Citra", 750_000))

bank.setor("001", 250_000)
bank.tarik("002", 100_000)
bank.setor("003", 50_000)
bank.tarik("003", 800_000)  

bank.tampilkan_semua_rekening()
