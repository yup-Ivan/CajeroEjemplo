from funciones.utiles import CashRegister

caja1 = CashRegister()
caja2 = CashRegister()
print(caja1.add(50, 'Ingreso por nomina'))
print(caja2.add(50, 'Ingreso por nomina'))
print(caja1.add(60, 'Ingreso por 10 eur que me he encontrado en la calle'))
print(caja1.add(-55, 'Cine 1'))
print(caja2.add(-5, 'Cine 1'))
print(caja1.add(-20, 'Cine 2'))
print(caja1.delete_last())
print(f'Total en tu cuenta: {caja1.balance}')
caja1.__str__()
caja2.__str__()