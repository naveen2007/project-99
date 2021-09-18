class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number


    def withdrawal(self, card_number):
            print("withdrawed 25")
    def balance(self, card_number):
            print("100")
    def deposit(self, card_number):
            print("deposited 25")

card = atm(231313, 12)
print(card.withdrawal(231313))