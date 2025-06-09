from dompet_digital import Dompet_Digital
from kartu_kredit import Kartu_Kredit
from tunai import Tunai

while True:
    print("SELAMAT DATANG DI SUPERMARKET")
    print("1. Pembayaran lewat dompet digital")
    print("2. Pembayaran lewat kartu kredit")
    print("3. Pembayaran lewat tunai")
    print("4. Keluar")

    jawab = int(input("Masukkan tipe pembayaran: "))
    if jawab == 1:
        Dompet_Digital().bayar()
        # pembayaran.bayar()  
    elif jawab == 2:
        Kartu_Kredit().bayar()
        # pembayaran.bayar()  
    elif jawab == 3:
        Tunai().bayar()
        # pembayaran.bayar()  
    elif jawab == 4:
        print("Terimakasih sudah berkunjung")
        break
    else:
        print("Pilihan tidak valid.")
        
        

