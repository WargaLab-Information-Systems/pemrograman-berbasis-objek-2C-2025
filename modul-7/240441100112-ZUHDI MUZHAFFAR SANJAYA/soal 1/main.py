from cash_payment import CashPayment
from credit_card_payment import CreditCardPayment
from ewallet_payment import EWalletPayment

def main():
    print("=== Simulasi Pembayaran ===")
    amount = float(input("Masukkan jumlah total belanja (Rp): "))

    print("\nPilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. Dompet Digital")
    
    choice = input("Pilihan Anda (1/2/3): ")
    
    if choice == "1":
        payment = CashPayment()
    elif choice == "2":
        payment = CreditCardPayment()
    elif choice == "3":
        payment = EWalletPayment()
    else:
        print("Metode tidak valid.")
        return
    
    payment.process_payment(amount)

if __name__ == "__main__":
    main()