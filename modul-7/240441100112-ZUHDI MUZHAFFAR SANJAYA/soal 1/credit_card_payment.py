from payment_interface import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        fee = 0.03  
        total = amount + (amount * fee)
        print(f"Pembayaran kartu kredit: Biaya tambahan 3% diterapkan.")
        print(f"Total yang dibayar: Rp {total:,.2f}")