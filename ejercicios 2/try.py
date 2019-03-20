try:
    dividendo =float( input("ingrese un numero para dividendo: "))
    divisor = float(input("ingres un numero para divisor: "))

    resultado = dividendo/divisor

    print('{0} es dividido por {1} y su resultado es {2}'.format(dividendo, divisor, resultado))

except ZeroDivisionError:
     print("'{1}' no es posible como divisor").format(divisor)

except ValueError:
     print("ingrese solo numeros")
