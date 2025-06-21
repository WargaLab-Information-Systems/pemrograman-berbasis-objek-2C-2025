class Pasien :
    def __init__(self,nama,umur,keluhan):
        self.__nama =nama
        self.__umur =umur
        self.__keluhan =keluhan
    
    def get_inpo (self):
        return f" nama :{self.__nama},umur: {self.__umur},keluhan :{self.__keluhan}"

class Klinik:
    def __init__(self):
        self.__daftar_pasien=[]

    def tambah_pasien (self,nama,umur,keluhan):
        pasien_baru =Pasien(nama,umur,keluhan)
        self.__daftar_pasien.append(pasien_baru)
        print(f"Pasien '{nama}' berhasil ditambahkan.")

    def tampilkan_pasien(self):
        if not self.__daftar_pasien:
            print("Belum ada pasien yang terdaftar.")
        else:
            print("Daftar Pasien di Klinik:")
            for index, pasien in enumerate(self.__daftar_pasien, start=1):
                print(f"{index}. {pasien.get_inpo()}")
def main():
    klinik = Klinik()

    klinik.tambah_pasien("Ayu", 28, "Demam dan sakit kepala")
    klinik.tambah_pasien("Budi", 35, "Sakit perut")
    klinik.tambah_pasien("Citra", 22, "Batuk dan pilek")

    print()
    klinik.tampilkan_pasien()

if __name__ == "__main__":
    main()
        