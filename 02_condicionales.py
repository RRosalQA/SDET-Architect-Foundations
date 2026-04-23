"""
Módulo 02: Lógica de Condicionales
Propósito: Ejercicios de validación, control de flujo y lógica booleana.
Autor: Richard Rosal
Fecha: Abril 2026
"""

# 1. Mayor de edad
preguntar_edad = int(input("Por favor, indique su edad: "))

if preguntar_edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")


# 2. Par o Impar
validar_par = int(input("Introduzca un numero para validar si es par: "))

if validar_par % 2 == 0:
    print("Este es un numero par")
else:
    print("Este numero es impar")


# 3. Comparación Simple
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ahora escriba el segundo numero: "))

if num1 > num2:
    print("El primer numero es mayor al segundo")
elif num1 < num2:
    print("El segundo numero es mayor que el primero")
else:
    print("Los dos numeros son iguales")


# 4. Positivo, Negativo o Cero
valor = int(input("Ingrese un numero a verificar: "))

if valor == 0:
    print("El numero es cero")
elif valor < 0:
    print("El numero es negativo")
else:
    print("El numero es positivo")


# 5. Aprobado o Reprobado
nota = int(input("Ingrese una calificacion, por favor: "))

if nota >= 10:
    print("Usted esta aprobado")
else:
    print("Usted esta reprobado")


# 6. Multiplicidad
cifra = int(input("Ingrese un numero, por favor: "))

if cifra % 5 == 0:
    print("El numero es divisible por 5")
else:
    print("El numero no es divisible por 5")


# 7. Login Simple
user = input("Ingrese su nombre de usuario, por favor: ").lower()

if user == "admin":
    print("Hola, Jefe")
else:
    print("Hola, Usuario")


# 8. Descuento de Tienda (Se añade 'else' para feedback del usuario)
monto_compra = float(input("Indique el monto de la compra, por favor: "))

if monto_compra > 100:
    descuento = monto_compra * 0.10
    print(f"La compra recibe un descuento de 10%. Total a pagar: {monto_compra - descuento}")
else:
    print(f"Total a pagar sin descuento: {monto_compra}")


# 9. Rango de Número
num_rango = int(input("Ingrese un numero entre 1 y 100: "))

if num_rango >= 1 and num_rango <= 100:
    print(f"El numero {num_rango} se encuentra entre 1 y 100")
else:
    print("El numero se encuentra fuera del rango solicitado")


# 10. Operador Not (Corregido para usar 'not' sobre un booleano)
hambre_input = input("¿Tiene hambre? (S/N): ").lower()
hambre = (hambre_input == "s")

if not hambre:
    print("No hay hambre. Estado: Satisfecho")
else:
    print("Aqui si hay hambre. Estado: Necesita comer")


# 11. Clasificador de Edad
user_age = int(input("Ingrese la edad, por favor: "))

if user_age < 13:
    print("Niño")
elif user_age >= 13 and user_age <= 17:
    print("Adolescente")
else:
    print("Adulto")


# 12. Calculadora
num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba ahora el segundo numero: "))
operacion = input("Ingrese el simbolo de la operacion (+, -, x, /): ")

if operacion == "+":
    print(f"Suma: {num1 + num2}")
elif operacion == "-":
    print(f"Resta: {num1 - num2}")
elif operacion == "x":
    print(f"Multiplicacion: {num1 * num2}")
else:
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Error: No se puede dividir entre cero")


# 13. Semáforo
semaforo = input("Introduzca el color del semaforo: ").lower()

if semaforo == "rojo":
    print("Detengase")
elif semaforo == "amarillo":
    print("Precaucion")
elif semaforo == "verde":
    print("Avance")
else:
    print("Color no reconocido")


# 14. Día de la Semana
dia_semana = int(input("Ingrese el numero del dia (1-7): "))

if dia_semana == 1:
    print("Lunes")
elif dia_semana == 2:
    print("Martes")
elif dia_semana == 3:
    print("Miercoles")
elif dia_semana == 4:
    print("Jueves")
elif dia_semana == 5:
    print("Viernes")
elif dia_semana == 6:
    print("Sabado")
elif dia_semana == 7:
    print("Domingo")
else:
    print("Error en el numero ingresado")


# 15. Notas Americanas 
nota = int(input("Ingrese la calificacion (0-20): "))

if nota >= 18:
    print("A")
elif nota >= 15:
    print("B")
elif nota >= 12:
    print("C")
elif nota >= 10:
    print("D")
else:
    print("F")


# 16. Validador de Texto
info = input("Introduzca informacion: ")

if info == "":
    print("Error: Campo requerido")
else:
    print("Informacion correctamente almacenada")


# 17. Estaciones del Año
mes = input("Introduce el nombre del mes: ").lower()

if mes == "enero" or mes == "febrero" or mes == "diciembre":
    print("Invierno")
elif mes == "marzo" or mes == "abril" or mes == "mayo":
    print("Primavera")
elif mes == "junio" or mes == "julio" or mes == "agosto":
    print("Verano")
else:
    print("Otoño")


# 18. Comparación de Cadenas
word1 = input("Escriba la primera palabra: ")
word2 = input("Escriba la segunda palabra: ")

if word1 == word2:
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")


# 19. Sistema de Peaje
vehiculo = input("Ingrese el tipo de vehiculo (moto, carro, camion): ").lower()

if vehiculo == "moto":
    print("Tarifa: $1")
elif vehiculo == "carro":
    print("Tarifa: $2")
else:
    print("Tarifa: $5")


# 20. Mayor de Tres
numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))
numero3 = int(input("Tercer numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El numero {numero1} es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero {numero2} es el mayor")
else:
    print(f"El numero {numero3} es el mayor")


# 21. Status Code QA 
codigo = int(input("Ingrese el codigo de error: "))

if codigo == 200:
    print("Exito")
elif codigo == 404:
    print("No encontrado")
elif codigo == 500:
    print("Error en el servidor")
else:
    print("Codigo desconocido")


# 22. Fuerza de Password
password = input("Ingrese su contraseña: ")

if len(password) < 8:
    print("Password debil")
else:
    print("Password fuerte")


# 23. Año Bisiesto
bisiesto = int(input("Ingrese año: "))

if (bisiesto % 4 == 0 and bisiesto % 100 != 0) or (bisiesto % 400 == 0):
    print(f"El año {bisiesto} es bisiesto")
else:
    print(f"El año {bisiesto} NO es bisiesto")


# 24. Verificador de Email
email = input("Ingrese un email: ").lower()

if "@" in email:
    print(f"Formato correcto")
else:
    print(f"Error: El email carece de @")


# 25. Login de Dos Pasos
usr_db = "admin"
pwd_db = 12345
user_in = input("Usuario: ").lower()
pwd_in = int(input("Contraseña: "))

if user_in == usr_db and pwd_in == pwd_db:
    print("Datos correctos. Acceso permitido")
else:
    print("Acceso denegado")


# 26. Simulador de Cajero
saldo = 20000
retiro = float(input("Monto a retirar: $ "))

if retiro <= saldo:
    print(f"Retiro aprobado. Saldo restante: ${saldo - retiro}")
else:
    print("Fondos insuficientes")


# 27. Tipo de Triángulo
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triangulo equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")


# 28. Calculadora IMC
altura = float(input("Altura (m): "))
peso = float(input("Peso (kg): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc <= 24.9:
    print("Peso normal")
elif imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")


# 29. Verificador de Palíndromo
word = input("Ingrese una palabra: ").lower()

if word == word[::-1]:
    print(f"La palabra {word} es palindroma")
else:
    print(f"La palabra {word} no es palindroma")


# 30. Orquestador de Pruebas
codigo_error = int(input("Codigo de error detectado: "))
prioridad = input("Prioridad (alta/baja): ").lower()
if codigo_error >= 500 and prioridad == "alta":
    reporte = "Urgente"
else:
    reporte = "Pendiente"
print(f"El bug con error {codigo_error} se ha marcado como: {reporte}")