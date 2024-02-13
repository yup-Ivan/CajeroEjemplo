from datetime import datetime
import time

class Movement:

    def __init__(self, number, datetime, amount, concept):
        self.number = number
        self.datetime = datetime
        self.amount = amount
        self.concept = concept

    def __str__(self):
        return f'Number: {self.number}, Datetime: {self.datetime}, Amount: {self.amount}, Concept: {self.concept}'

class CashRegister:

    id_transaction = 3

    def __init__(self):
        self.movimientos = []
        self.negativo = lambda x: x < 0
        self.saldo_insuficiente = lambda x: self.balance + x < 0
        self.id_transaction = 0

    def add(self, amount, concept):
        time.sleep(0.001) # Hago esto simplemente para que haya una diferencia temporal REAL entre cada transaccion.
        if self.negativo(amount) and self.saldo_insuficiente(amount):
            return 'No tienes suficiente dinero.'
        new_mov = Movement(CashRegister.id_transaction, datetime.now(), amount, concept)
        self.movimientos.append(new_mov)
        CashRegister.id_transaction += 1
        return f'Se ha agregado el pago: {new_mov.concept}, con importe: {new_mov.amount}.'

    def delete_last(self):
        if not self.movimientos:
            return "No hay transacciones."
        return f'Se ha eliminado la transaccion: {self.movimientos.pop()}'

    @property
    def balance(self):
        return sum(movimiento.amount for movimiento in self.movimientos)

    def __str__(self):
        for movimiento in self.movimientos:
            print(movimiento.__str__())