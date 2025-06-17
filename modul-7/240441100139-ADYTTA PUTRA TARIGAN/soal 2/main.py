from mobil import Mobil
from motor import Motor
from sepeda import Sepeda

def simulasi_booking(kendaraan, nama, usia):
    hasil = kendaraan.proses_booking(nama, usia)
    print(hasil)
    if "berhasil" in hasil:
        print(f"Biaya: {kendaraan.hitung_biaya()}")
        print(kendaraan.info_asuransi())

def main():
    try:
        jumlah_user = int(input("Masukkan jumlah pengguna yang ingin booking: "))
        kendaraan_list = [Mobil(), Motor(), Sepeda()]

        for i in range(jumlah_user):
            print(f"\n--- Pengguna {i+1} ---")
            nama = input("Nama: ")
            usia = int(input("Usia: "))

            print(f"\nSimulasi booking untuk {nama} (usia {usia})")
            for kendaraan in kendaraan_list:
                simulasi_booking(kendaraan, nama, usia)

    except ValueError:
        print("Input tidak valid. Pastikan usia dan jumlah pengguna berupa angka.")

if __name__ == "__main__":
    main()