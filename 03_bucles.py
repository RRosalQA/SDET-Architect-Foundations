"""
Módulo 03: Fundamentos de Python - Bucles (Loops)
Propósito: Práctica de iteraciones controladas (for) y condicionales (while) para QA Automation.
Autor: Richard Rosal
Fecha: Abril 2026
"""

# 01. Imprimir números del 1 al 10 con `for`.
for i in range(1, 11):
    print(i)


# 02. Imprimir números del 10 al 1 con `while`.
num = 10

while num >= 1:
    print(num)
    num -= 1


# 03. Sumar los primeros 50 números naturales.
num = 1
sum = 0

while num <= 50:
    sum += num
    num += 1
print(sum)


# 04. Imprimir solo los números pares del 1 al 20.
for num in range(1, 21):
    if num % 2 == 0:
        print(num)
    else:
        continue


# 05. Generar la tabla de multiplicar de un número dado.
tabla = int(input("Indique la tabla de multiplicar a generar: "))

for i in range(1, 11):
    print(f"{tabla} X {i} es igual a {tabla * i}")
