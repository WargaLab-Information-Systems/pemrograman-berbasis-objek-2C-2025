from payment_interface import PaymentMethod

class EWalletPayment(PaymentMethod):
    def process_payment(self, amount):
        cashback = 0.02  
        total = amount - (amount * cashback)
        print(f"Pembayaran dompet digital: Cashback 2% diberikan.")
        print(f"Total yang dibayar: Rp {total:,.2f}")