class Pasien:
    def __init__(self, nama, umur, keluhan):
        if not isinstance(nama, str) or not nama.strip() or nama.isdigit():
            raise ValueError("Nama harus berupa string, tidak boleh kososng, dan tidak mengandung angka")
        if not isinstance(umur, (int, float)) or umur <= 0:
            raise ValueError("Umur harus angka dan lebih besar dari 0")
        if not isinstance(keluhan, str) or not keluhan.strip():
            raise ValueError("Keluhan harus berupa string, dan tidak boleh kosong")
        
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    @property
    def nama(self):
        return self.__nama
    
    @property
    def umur(self):
        return self.__umur
    
    @property
    def keluhan(self):
        return self.__keluhan
    
class Klinik:
    data_pasien = []

    @classmethod
    def tambah(cls, pasien):
        cls.data_pasien.append(pasien)

    @classmethod
    def display(cls):
        print("\n=====DATA PASIEN=====")
        for pasien in cls.data_pasien:
            print(f"Nama   : {pasien.nama}")
            print(f"Umur   : {pasien.umur} tahun")
            print(f"Keluhan: {pasien.keluhan}")
            print()

def main():
    try:
        pasien1 = Pasien("Amin", 19, "Sakit Gigi")
        pasien2 = Pasien("Alexei", 50, "Sakit Perut")
        pasien3 = Pasien("Ava", 35, "Pusing")

        Klinik.tambah(pasien1)
        Klinik.tambah(pasien2)
        Klinik.tambah(pasien3)

        Klinik.display()
    except ValueError as a:
        print(f"Error: {a}")

if __name__ == "__main__":
    main()