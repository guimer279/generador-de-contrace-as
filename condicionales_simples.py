print("sistema para calcular el promedio de un alumno")

nombre = input("para comenzar, ¿cual es tu nombre? ")

matematicas = int(input(nombre + " ¿cual es la calificacion en matematicas?: "))
quimica = int(input(nombre + "¿cula es la calificacion de quimica?: "))
fisica = int(input(nombre + "¿cual es la calificacion de quimica?: "))

promedio = (matematicas + quimica + fisica) / 3
promedio = int(promedio)

if promedio >= 6:
    print('felicidades ' + nombre + '" aprobaste" con un promedio de: ', promedio)

print("fin.")
