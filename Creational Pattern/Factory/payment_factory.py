from abc import ABC, abstractmethod
# Product Interface

class Payment(ABC):

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete Products

class CreditCardPayment(Payment):

    def pay(self, amount: float) -> None:
        print(f"Processing Credit Card payment of ${amount}")
        print("✔ Charging card...")
        print("✔ Payment successful via Credit Card\n")


class PayPalPayment(Payment):

    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")
        print("✔ Redirecting to PayPal...")
        print("✔ Payment successful via PayPal\n")


class TelebirrPayment(Payment):

    def pay(self, amount: float) -> None:
        print(f"Processing Telebirr payment of ${amount}")
        print("✔ Connecting to Telebirr API...")
        print("✔ Payment successful via Telebirr\n")


# Creator (Factory)
class PaymentFactory(ABC):

    @abstractmethod
    def create_payment(self) -> Payment:
        pass

    def process_payment(self, amount: float) -> None:
        payment = self.create_payment()
        payment.pay(amount)

# Concrete Factories

class CreditCardFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return CreditCardPayment()


class PayPalFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return PayPalPayment()


class TelebirrFactory(PaymentFactory):
    def create_payment(self) -> Payment:
        return TelebirrPayment()

#client code

def client_code(factory: PaymentFactory, amount: float):
    factory.process_payment(amount)


if __name__ == "__main__":

    print("=== Payment System ===")
    print("Choose Payment Method:")
    print("1 - Credit Card")
    print("2 - PayPal")
    print("3 - Telebirr")

    choice = input("Enter choice (1/2/3): ")
    amount = float(input("Enter amount: "))

    if choice == "1":
        factory = CreditCardFactory()
        print("\nApp: Using Credit Card Payment")

    elif choice == "2":
        factory = PayPalFactory()
        print("\nApp: Using PayPal Payment")

    elif choice == "3":
        factory = TelebirrFactory()
        print("\nApp: Using Telebirr Payment")

    else:
        print(" Invalid choice!")
        exit()

    factory.process_payment(amount)