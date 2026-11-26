#Pedir peso y estatura a la persona
print("Bienvenido a la calculadora de IMC")
name = (input("Ingrese su nombre: "))
weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su estatura en metros: "))
#multiplicar la estatura por estatura y dividir el peso en ese resultado
imc = weight / (height**2)
#imprimir el resultado
print(f"{name}, tu IMC es: {imc:.1f}")


# Uso de condicionales para determinar si esta en sobrepeso,obesidad, bajo de peso o normal
if imc < 18.5:
    print("Estas bajo de peso y no es bueno para tu salud")
elif 18.5 <= imc < 25:
    print("Tu peso es normal y saludable")
elif 25 <= imc < 30:
    print("Estas en sobrepeso y no es bueno para tu salud")
else:
    print("Estas en obesidad y no es bueno para tu salud")
    