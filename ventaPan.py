x=50
y=0

Venta=int(input('Ingresa la venta de pan: '))

Porcentaje= Venta * 100 / 50

print(f'El porcentaje es: {Porcentaje} %')

if Porcentaje <= 25:
    print("Muy poca venta")
if Porcentaje >= 26 and Porcentaje <=50:
    print("Poca venta")
if Porcentaje >= 51 and Porcentaje <=75:
    print("Venta aceptable")
if Porcentaje >=76 and Porcentaje <=99:
    print("Bastante venta")
if Porcentaje >= 100:
    print("Mucha venta")
