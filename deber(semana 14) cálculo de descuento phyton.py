def calcular_descuento(monto_total, descuento= 10):
    monto_descuento = (monto_total* descuento) /100
    return monto_descuento
valor_subtotal= 120
porcentaje_descuento = 20

valor_descuento = calcular_descuento(valor_subtotal)
valor_total= valor_subtotal-valor_descuento
print(f'total={valor_total}. luego de un descuento de {valor_descuento}. aplicando el 10% al subtotal de {valor_subtotal}')

valor_subtotal= float(input('ingrese el subtotal:'))
porcentaje_descuento = int(input('ingrese el porcentaje de descuento:'))

valor_descuento = calcular_descuento(valor_subtotal, porcentaje_descuento)
valor_total= valor_subtotal-valor_descuento
print(f'total={valor_total}. luego de un descuento de {valor_descuento}. aplicando el {porcentaje_descuento}% al subtotal de {valor_subtotal}')