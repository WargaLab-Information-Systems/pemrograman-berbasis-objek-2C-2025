from payment_interface import PaymentMethod

class CashPayment(PaymentMethod):
    def process_payment(self, amount):
        discount = 0.05  
        total = amount - (amount * discount)
        print(f"Pembayaran tunai: Diskon 5% diterapkan.")
        print(f"Total yang dibayar: Rp {total:,.2f}")