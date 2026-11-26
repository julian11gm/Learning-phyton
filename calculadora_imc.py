#Pedir peso y estatura a la persona
print("Bienvenido a la calculadora de IMC")
name = (input("Ingrese su nombre: "))
weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su estatura en metros: "))
#multiplicar la estatura por estatura y dividir el peso en ese resultado
imc = weight / (height**2)
#imprimir el resultado
print(f"{name}, tu IMC es: {imc:.1f}")
