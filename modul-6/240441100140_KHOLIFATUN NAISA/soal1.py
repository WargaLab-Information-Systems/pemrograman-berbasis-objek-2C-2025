class BangunDatar:
    def luas(self):
        pass

class Persegi(BangunDatar):
    def luas(self):
        sisi = int(input("masukkan sisi dari persegi: "))
        L = sisi * sisi
        return(f"- luas dari persegi dengan sisi {sisi} adalah {L}")
class Lingkaran(BangunDatar):
    def luas(self):
        jari_jari = int(input("masukkan jari-jari dari lingkaran: "))
        L = 3.14 * (jari_jari**2)
        return(f"- luas dari lingkaran dengan jari-jari {jari_jari} adalah {L}")
class Segitiga(BangunDatar):
    def luas(self):
        alas = int(input("masukkan alas dari segitiga: "))
        tinggi = int(input("masukkan tinggi dari segitiga: "))
        L = 1/2 * alas * tinggi
        return(f"- luas dari Segitiga dengan alas {alas} dan tinggi {tinggi} adalah {L}")

menyimpandata = []
def jawaban(hasil):
    hasil_luas = hasil.luas()
    print(hasil_luas)
    menyimpandata.append(hasil_luas)

while True:
    print("\nSELAMAT DATANG DI HITUNG MENGHITUNG")
    print ("1. Persegi")
    print ("2. Lingkaran")
    print ("3. Segitiga")
    print ("4. tampilkan info")
    print ("5. keluar")

    jawab = int(input("Masukkan nomor yang anda ingin hitung: "))
    if jawab == 1:
        persegi = Persegi()
        jawaban(persegi)
    elif jawab == 2:
        lingkaran = Lingkaran()
        jawaban(lingkaran)
    elif jawab == 3:
        segitiga = Segitiga()
        jawaban(segitiga)
    elif jawab == 4:
        if menyimpandata:
            print("\nData yang sudah dihitung:")
            for data in (menyimpandata) :
                print(data)
        else:
            print("Belum ada data yang disimpan.")
    elif jawab == 5:
        print("Terima kasih telah menggunakan layanan hitung menghitung.")
        break
    else:
        print("nomor yang anda inputkan tidak valid")
 




