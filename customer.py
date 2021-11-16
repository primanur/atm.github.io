from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custSaldo = 10000):
        self.id = id
        self.pin = custPin
        self.saldo = custSaldo
    
    def checkId(self):
        return self.id
    
    def checkPin(self):
        return self.pin
    
    def checkSaldo(self):
        return self.saldo

    def debetSaldo(self, nominal):
        self.saldo -= nominal    
    
    def depositSaldo(self, nominal):
        self.saldo += nominal    
