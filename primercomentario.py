#las cosas las soltamos con print

print("hola julio")

#Variables

Julian = 67
lis = 60

print(Julian + lis)


#Listas= se pueden modificar y tambien llamado de posiciones
name23 = "Lebron"
name24 = "James"
name25 = "Antetokounmpo"
my_list1 = [name23, name24, name25]
print(my_list1)

#Esto es una interpolacion de variables va entre llaves y se pone una f antes de las comillas
print(f"el mejor jugador es {my_list1[0]}")

# Diccionario

#A la hora de imprimir una lista o diccionario se debe usar la funcion type con print y volverla a imprimir para ver que tipo de dato es


My_dict = {"BB":name23,"YOUV":name24,"OPA":name25}
print(type(My_dict))
print(My_dict)
print(f"el peor jugador es {My_dict['BB']}")

#Se le pueden colocar contraseñas y de esa manera se llama el dato que se quiere

#Tuplas o sets
#Son aquellas que no se repiten y no se pueden modificar, se usan para guardar datos que no se van a cambiar

tupla1 = ("Lebron", "James", "Antetokounmpo")
print(type(tupla1))
print(tupla1)


# If/else
if name23 == "Lebron":
    print("El mejor jugador es Lebron")
    




