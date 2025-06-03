from abc import ABC, abstractmethod

class Manusia(ABC):
    @abstractmethod
    def berbicara(self):
        pass

    @abstractmethod
    def bekerja(self):
        pass

    @abstractmethod
    def makan(self):
        pass

class Joko(Manusia):
    def berbicara(self):
        print("Joko: Halo, saya suka berbicara tentang politik!")

    def bekerja(self):
        print("Joko: Saya bekerja sebagai petani di desa.")

    def makan(self):
        print("Joko: Saya suka makan pecel lele!")

class Beni(Manusia):
    def berbicara(self):
        print("Beni: Hai, aku lebih suka ngobrol tentang game!")

    def bekerja(self):
        print("Beni: Aku adalah seorang developer game indie.")

    def makan(self):
        print("Beni: Makanan favoritku adalah ramen!")

class Fani(Manusia):
    def berbicara(self):
        print("Fani: Hai semuanya, aku senang ngobrol tentang fashion!")

    def bekerja(self):
        print("Fani: Aku bekerja sebagai fashion designer.")

    def makan(self):
        print("Fani: Aku suka makan salad buah segar!")

class Jani(Manusia):
    def berbicara(self):
        print("Jani: Halo, aku suka bicara tentang teknologi dan sains.")

    def bekerja(self):
        print("Jani: Aku bekerja di laboratorium riset AI.")

    def makan(self):
        print("Jani: Aku doyan banget makan nasi goreng kampung!")

def tampilkan_aktivitas(obj):
    obj.berbicara()
    obj.bekerja()
    obj.makan()

print("Pilih karakter untuk ditampilkan aktivitasnya:")
print("1. Joko")
print("2. Beni")
print("3. Fani")
print("4. Jani")
print("5. Tambah karakter sendiri")

pilihan = input("Masukkan nomor pilihan (1-5): ")

if pilihan == "1":
    print("\n=== Aktivitas Joko ===")
    joko = Joko()
    tampilkan_aktivitas(joko)

elif pilihan == "2":
    print("\n=== Aktivitas Beni ===")
    beni = Beni()
    tampilkan_aktivitas(beni)

elif pilihan == "3":
    print("\n=== Aktivitas Fani ===")
    fani = Fani()
    tampilkan_aktivitas(fani)

elif pilihan == "4":
    print("\n=== Aktivitas Jani ===")
    jani = Jani()
    tampilkan_aktivitas(jani)

elif pilihan == "5":
    print("\n=== Tambah Karakter Baru ===")
    nama = input("Masukkan nama karakter: ")
    bicara = input(f"Pembicaraan favoritnya apa?")
    kerja = input(f"Bekerja sebagai apa? ")
    makan = input(f"Suka makan apa? ")

    class KarakterKustom(Manusia):
        def berbicara(self):
            print(f"{nama}: Hai, aku suka berbicara tentang {bicara}.")

        def bekerja(self):
            print(f"{nama}: Aku bekerja sebagai {kerja}.")

        def makan(self):
            print(f"{nama}: Aku suka makan {makan}!")

    print(f"\n=== Aktivitas {nama} ===")
    karakter = KarakterKustom()
    tampilkan_aktivitas(karakter)

else:
    print("Pilihan tidak valid.")