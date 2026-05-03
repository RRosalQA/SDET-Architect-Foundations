""""# 1. Validador de Login QA
usuario_registrado = "admin"
clave_registrada = "1234"


usuario_user = input("Ingrese su usuario, por favor: ")
usuario_clave = input("Ahora, ingrese su contraseña: ")


if usuario_user == usuario_registrado and usuario_clave == clave_registrada:
    print("Acceso concedido al Sistema de Pruebas")
elif usuario_user != usuario_registrado:
    print("Usuario no reconocido")
else:
    print("Contraseña incorrecta")


# 2. Rango de temperatura de servidor
temperatura_actual = int(input("Ingrese la temperatura del servidor: "))


if temperatura_actual >= 18 and temperatura_actual <= 25:  # Se que hay formas de hacer esto de mejor manera 
    print("Temperatura optima")
elif temperatura_actual < 18:
    print("Activando calefaccion")
else:
    print("Activando ventilacion de emergencia")


# 3. Calculadora de año bisiesto
anio = int(input("Introduzca el año a verificar: "))


if anio % 4 == 0 and anio % 100 != 0:
    print("Año apto para reporte bisiesto")
else:
    print("Año estandar")


# 4. Comparador de versiones de software
num1 = int(input("Dime el primer numero de la version: "))
num2 = int(input("Ahora dime el numero de la otra version: "))


if num1 == num2:
    print("Las versiones de software son iguales")
elif num1 > num2:
    print("La primera version es mayor que la segunda")
else:
    print("La segunda version es mayor que la primera")


# 5. Simulador de cajero (ATM)
saldo = 1000


dinero = int(input("Indique cuanto dinero desea retirar: "))

if dinero > saldo:
    print("Fondos insuficientes")
elif dinero < 0:
    print("Operacion no valida")
else:
    print(f"Operacion aprobada por {dinero}. Saldo restant: ${saldo - dinero}.")
    

# 6. Triangulos en el diseño
lado1 = int(input("Ingrese el valor del primer lado: "))
lado2 = int(input("Ingrese ahora el valor del segundo lado: "))
lado3 = int(input("Finalmente, ingrese el valor del tercer lado del triangulo: "))

"""

age = 36
txt = "My name is John and I am" + age
print(txt)
