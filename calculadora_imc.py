#Pedir peso y estatura a la persona

print("Bienvenido a la calculadora de IMC")
name = input("Ingrese su nombre: ")

try:
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su estatura en metros: "))
except ValueError:
    print("Por favor ingrese sus datos en decimales, no en letras.")
else:
 
# Calcular el IMC: peso / estatura al cuadrado.
 
    imc = weight / (height**2)
    print(f"{name}, tu IMC es: {imc:.1f}")
    
    # Uso de condicionales para determinar si esta en sobrepeso,obesidad o bajo de peso y mostrar un mensaje al usuario
    
    if imc < 18.5:
        print("Estas bajo de peso y no es bueno para tu salud")
    elif 18.5 <= imc < 25:
        print("Tu peso es normal y saludable")
    elif 25 <= imc < 30:
        print("Estas en sobrepeso y no es bueno para tu salud")
    else:
        print("Estas en obesidad y no es bueno para tu salud")
        